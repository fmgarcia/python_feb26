# Quiero crear un proyecto que haga lo siguiente:
# 0. Generación de claves globales y keys de APIS y fichero .env
# 1. Me quiero conectar a una API de fútbol (por ejemplo, la API de football-data.org) para obtener información sobre los equipos.
# 2. Quiero crear una clase llamada "Equipo" que tenga atributos como nombre, estadio, etc. (atributos que pueda coger de la API)
# 2.1 Quiero hacer uso de la librería pydantic para validar los datos que me llegan de la API y asegurarme de que cumplen con el formato esperado.
# 3. Quiero poder almacenar los datos en una base de datos (por ejemplo, MySql) y luego poder consultarlos.
# Todo estará orquestado desde un main principal que se encargará de llamar a las funciones necesarias para realizar cada una de las tareas mencionadas.

from dotenv import load_dotenv
import os
import requests
from pydantic import BaseModel, Field
from typing import Optional
import mysql.connector
from mysql.connector import Error

# Paso 0.
load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY") # Reemplaza con tu token de autenticación de la API de fútbol
BASE_URL = "https://api.football-data.org/v4/"
BASE_EQUIPOS_URL = f"{BASE_URL}teams/"
BASE_COMPETICIONES_URL = f"{BASE_URL}competitions/"
CONFIGURATION_DB = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306))
}

# Paso 2. Clase Equipo con validación de datos usando pydantic para asegurar que los datos cumplen con el formato esperado
# La clase Equipo hereda de BaseModel, lo que permite utilizar las funcionalidades de validación de datos de pydantic. Cada atributo de la clase tiene una anotación de tipo y un Field que especifica las restricciones y alias para los campos que se esperan recibir de la API.
# Paso 2.1 Pydantic validará automáticamente los datos que se le pasen al crear una instancia de la clase Equipo. Si los datos no cumplen con las restricciones definidas en los Field, se lanzará una excepción indicando qué campo no cumple con el formato esperado.

class Equipo(BaseModel):
    id_equipo: int = Field(..., gt=0, alias="id")
    nombre: str = Field(..., max_length=100, alias="name")
    nombre_corto: Optional[str] = Field(..., max_length=50, alias="shortName")
    tla: Optional[str] = Field(..., max_length=3, alias="tla")
    fundacion: Optional[int] = Field(..., ge=1800, le=2026, alias="founded")
    estadio: Optional[str] = Field(..., max_length=100, alias="venue")
    
    def __str__(self):
        return f"Equipo(id_equipo={self.id_equipo}, nombre='{self.nombre}', nombre_corto='{self.nombre_corto}', tla='{self.tla}', fundacion={self.fundacion}, estadio='{self.estadio}')"



# Paso 1. Función para obtener información sobre los equipos de una competición específica
def obtener_equipos_competicion(headers, id_competicion):
    url = f"{BASE_COMPETICIONES_URL}{id_competicion}/teams"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        equipos_competicion = response.json()
        equipos = [Equipo.model_validate(equipo) for equipo in equipos_competicion.get("teams", [])] # Validación de datos usando pydantic, si los datos no cumplen con el formato esperado, se lanzará una excepción. Cojo el campo "teams" del JSON que es una lista de equipos y creo una instancia de la clase Equipo para cada uno de ellos, validando los datos en el proceso.
        return equipos
    else:
        raise Exception(f"Error al obtener los datos de la API: {response.status_code} - {response.text}")

# Paso 3. Función para almacenar los datos en una base de datos MySQL
def almacenar_equipos_db(equipos):
    try:
        conexion = mysql.connector.connect(**CONFIGURATION_DB) # Establece la conexión a la base de datos utilizando los parámetros definidos en CONFIGURATION_DB a través de mysql.connector.connect(). Si la conexión es exitosa, se imprime un mensaje indicando que la conexión a la base de datos se ha establecido correctamente. ** CONFIGURATION_DB es una forma de pasar los parámetros de configuración como argumentos de palabra clave a la función connect().
        if conexion.is_connected():
            cursor = conexion.cursor() # Crea un cursor para ejecutar consultas SQL. El cursor es un objeto que permite interactuar con la base de datos y ejecutar comandos SQL.
            crear_tabla_query = """
            CREATE TABLE IF NOT EXISTS equipos (
                id_equipo INT PRIMARY KEY,
                nombre VARCHAR(100),
                nombre_corto VARCHAR(50),
                tla VARCHAR(3),
                fundacion INT,
                estadio VARCHAR(100)
            )
            """
            cursor.execute(crear_tabla_query) # Ejecuta la consulta SQL para crear la tabla "equipos" si no existe. La tabla tiene columnas que corresponden a los atributos de la clase Equipo, con tipos de datos adecuados para cada uno.

            guardados = 0
            for equipo in equipos:
                # Compruebo si el equipo ya existe en la base de datos para evitar duplicados. Esto se hace ejecutando una consulta SQL SELECT para verificar si ya existe un registro con el mismo id_equipo. Si no existe, se inserta el nuevo equipo en la base de datos utilizando una consulta SQL INSERT.
                cursor.execute(
                    "SELECT id_equipo FROM equipos WHERE id_equipo = %s",
                    (equipo.id_equipo,)
                )
                if not cursor.fetchone(): # Si no se encuentra el equipo, lo insertamos
                    guardados += 1
                    cursor.execute(
                        "INSERT INTO equipos (id_equipo, nombre, nombre_corto, tla, fundacion, estadio) VALUES (%s, %s, %s, %s, %s, %s)",
                        (equipo.id_equipo, equipo.nombre, equipo.nombre_corto, equipo.tla, equipo.fundacion, equipo.estadio)
                    )
            conexion.commit() # Confirma los cambios realizados en la base de datos. Esto es necesario para que las inserciones de datos se guarden de manera permanente en la base de datos. Si no se llama a commit(), los cambios no se guardarán y se perderán al cerrar la conexión.
            print(f"Datos almacenados en la base de datos correctamente. Se han guardado {guardados} equipos.")
        
    except Error as e:
        print(f"Error de base de datos: {e}")
        conexion.rollback() # Si ocurre un error durante la conexión o la ejecución de las consultas SQL, se llama a rollback() para deshacer cualquier cambio realizado en la base de datos durante la transacción actual. Esto asegura que la base de datos no quede en un estado inconsistente debido a errores.
    finally:
        # Asegurarnos de cerrar la conexión a la base de datos para liberar recursos, incluso si ocurre un error durante el proceso.
        if conexion.is_connected():
            cursor.close() # Cierra el cursor para liberar recursos asociados con él.
            conexion.close() # Cierra la conexión a la base de datos para liberar recursos asociados con la conexión.


if __name__ == "__main__":
    headers = {
    "X-Auth-Token": API_KEY # Reemplaza con tu token de autenticación de la API de fútbol
    }  
    try:
        competiciones = [2014,2017,2003]
        for id_competicion in competiciones:
            equipos = obtener_equipos_competicion(headers, id_competicion=id_competicion)
            almacenar_equipos_db(equipos)
    except Exception as e:
        print(f"Error al obtener los datos de la API: {e}")  
