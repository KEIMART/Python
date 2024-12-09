import requests

def enviar_cheep(mensaje):
    """Envía un nuevo cheep a la API."""
    url = "https://TU_URL_AQUI/send_cheep"  # Reemplaza con la URL proporcionada por tu instructor
    response = requests.post(url, json={"message": mensaje})
    if response.status_code == 200:
        print("Cheep enviado correctamente!")
    else:
        print(f"Error al enviar cheep: {response.status_code}")

def obtener_cheeps():
    """Obtiene todos los cheeps de la API."""
    url = "https://TU_URL_AQUI/get_cheeps"
    response = requests.get(url)
    if response.status_code == 200:
        cheeps = response.json()
        print("Lista de cheeps:")
        for cheep in cheeps:
            print(cheep["mensaje"])  # Asume que el mensaje está en un campo llamado "mensaje"
    else:
        print(f"Error al obtener cheeps: {response.status_code}")

# Ejemplo de uso:
enviar_cheep("¡Hola, mundo desde mi primer cheep!")
obtener_cheeps()