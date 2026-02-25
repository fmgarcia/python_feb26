from time import sleep
import requests
import json

url_base = "https://api.football-data.org/v4/teams/"

id_inicial = 85 # ID inicial para la primera persona
id_final = 90 # ID final para la última persona

headers = {
    "X-Auth-Token": "6bff5b66e01940a4a4730dad785bbab3" # Reemplaza con tu token de autenticación de la API de fútbol
}

equipos = [] # Creo una lista inicialmente vacía para almacenar los diccionarios de cada equipo obtenida de la API

for equipo in range(id_inicial, id_final + 1): # Procesa y guarda la información de cada equipo en la lista equipos, iterando desde el ID inicial hasta el ID final (inclusive)
    try:
        url = f"{url_base}{str(equipo)}" # Construye la URL completa para cada equipo utilizando el ID actual en la iteración
        response = requests.get(url, headers=headers) # realiza una solicitud GET a la URL de cada persona y almacena la respuesta en la variable response
        data = response.json()
        if data["name"]:
            equipos.append(data) # agrega el diccionario del equipo a la lista equipos        
        sleep(6) # Agrega una pausa de 6 segundos entre cada solicitud para evitar exceder los límites de la API
    except Exception as e:
        print(f"Error al obtener datos para el equipo con ID {equipo}") # Imprime un mensaje de error si ocurre una excepción durante la solicitud o el procesamiento de los datos para un equipo específico

# Guardo la lista de equipos en un fichero
with open("equipos.json", "w") as f:
    json.dump(equipos, f, indent=4) # Guarda la lista de equipos en un archivo JSON llamado "equipos.json" con una indentación de 4 espacios para mejorar la legibilidad