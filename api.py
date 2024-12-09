import requests

def trivia_fetch(num):
   
    try:
        respuesta = requests.get(f"http://numbersapi.com/{num}?json")
        respuesta.raise_for_status()
        datos = respuesta.json()
        return {
            "number": num,  
            "trivia": datos.get("text") 
        }
    except requests.RequestException as e:
        return {"error": str(e)}

def main():
    
    print("Hello learners!")
    print("¡Bienvenidos al cuestionario de trivia de números!")
    
    while True:
        try:
            
            num = int(input("Por favor, ingresa un número para aprender algo curioso (o escribe -1 para salir): "))
            
            if num == -1:
                print("¡Gracias por usar el cuestionario de trivia! ¡Hasta luego!")
                break
            
            trivia = trivia_fetch(num)
            
            if "error" in trivia:
                print(f"Ocurrió un error al obtener la trivia: {trivia['error']}")
            else:
                print(f"Trivia sobre el número {trivia['number']}: {trivia['trivia']}")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()
