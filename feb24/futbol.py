from time import sleep
import requests

url_base = "https://api.football-data.org/v4/teams/"

id_inicial = 85 # ID inicial para la primera persona
id_final = 90 # ID final para la última persona

headers = {
    "X-Auth-Token": "6bff5b66e01940a4a4730dad785bbab3" # Reemplaza con tu token de autenticación de la API de fútbol
}

for equipo in range(id_inicial, id_final + 1): # Itera desde el ID inicial hasta el ID final (inclusive)
    try:
        url = f"{url_base}{str(equipo)}" # Construye la URL completa para cada equipo utilizando el ID actual en la iteración
        response = requests.get(url, headers=headers) # realiza una solicitud GET a la URL de cada persona y almacena la respuesta en la variable response
        data = response.json()
        print(f"Nombre del equipo: {data['name']}") # imprime el nombre del equipo obtenido de la API
        print(f"Estadio: {data['venue']}") # imprime el estadio del equipo obtenido de la API
        if data['coach']['firstName'] is None: 
            print("Entrenador: No disponible") # Si el nombre del entrenador no está disponible, imprime un mensaje indicando que no se dispone de esa información
        else:
            print(f"Entrenador: {data['coach']['firstName']} {data['coach']['lastName']}") # imprime el nombre del entrenador del equipo obtenido de la API
        jugadores = data['squad'] # obtiene la lista de jugadores del equipo del diccionario data
        for jugador in jugadores:
            print(f"Jugador: {jugador['name']}, Posición: {jugador['position']}") # imprime el nombre y la posición de cada jugador del equipo obtenido de la API
        sleep(6) # Agrega una pausa de 6 segundos entre cada solicitud para evitar exceder los límites de la API
    except Exception as e:
        print(f"Error al obtener datos para el equipo con ID {equipo}") # Imprime un mensaje de error si ocurre una excepción durante la solicitud o el procesamiento de los datos para un equipo específico