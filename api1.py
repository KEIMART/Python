import requests
import json

url = "https://3bda700d-ebe7-421a-bbc1-20cb9289f0cc-00-c4yvkdzp1nlg.janeway.replit.dev/"
sendCheep = f"{url}/send_cheep"
getCheep = f"{url}/get_cheeps"

def sm(mensaje):
    try:
        response = requests.post(sendCheep, json={"message": mensaje})
        if response.status_code == 200:
            print("Mensaje enviado")
        else:
            print(f"Error al enviar mensaje: {response.status_code}")
    except Exception as e:
        print(f"Error al conectar a la API: {e}")

def om():
    try:
        response = requests.get(getCheep)
        if response.status_code == 200:
            cheeps = response.json()
            print("Lista de mensajes:")
            for idx, cheep in enumerate(cheeps, start=1):
                print(f"{idx}. {cheep}")
        else:
            print(f"error al obtener mensajes: {response.status_code}")
    except Exception as e:
        print(f"error al conectar api: {e}")

def mostrar_menu():
    while True:
        print("Super")
        print("1. Enviar mensaje")
        print("2. Ver todos los mensajes")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mensaje = input("Escribe tu mensaje: ")
            sm(mensaje)
        elif opcion == "2":
            om()
        elif opcion == "3":
            print("Hasta luego")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    mostrar_menu()
