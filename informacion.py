name = input("ingresa tu nombre: ")
lastname = input("ingresa tu apellido: ")

print(f"Hola, {name} {lastname}. Bienvenido a nuestra app.")

country = input("ingresa tu Pais: ")
city = input("ingresa tu Ciudad: ")

dateofbirth = input("¿En que año naciste?")

if int(dateofbirth) >= 1000:
    age = 2024 - int(dateofbirth)
    print(f"Tienes {age} anos.")

    if age >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
else:
    print("La fecha ingresada no es valida.")

nombre_completo = f"{name} {lastname}"
print(f"{nombre_completo} vive en {country} en la ciudad de {city}  y su edad es {age}")
