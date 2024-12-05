"""1.	Conversión de metros a centímetros
Escribe un programa que pida al usuario un número en metros y lo convierta a centímetros.
Ejemplo:
Entrada: Introduce la longitud en metros: 2
Salida: La longitud en centímetros es: 200 cm
"""

metros = float(input("Introduce la longitud en metros:"))
centimetros = metros * 100

print(f"La longitud en centimetros es : {centimetros} cm")

"""2.	Edad en el futuro
Crea un programa que pida el nombre del usuario y su edad. Luego, calcula cuántos años tendrá en 10 años.
Ejemplo:
Entrada:
Introduce tu nombre: Ana
Introduce tu edad: 25
Salida:
Hola Ana, en 10 años tendrás 35 años.
"""

nombre = input("introduce tu nombre: ")
edad = int(input("introduce tu edad: "))

edad_futura = edad + 10 

print(f"Hola {nombre}, en 10 años tendras {edad_futura} años.")

"""3.	Área de un rectángulo
Pide al usuario que introduzca la base y la altura de un rectángulo, y muestra el área calculada.
Ejemplo:
Entrada:
Base: 5
Altura: 3
Salida:
El área del rectángulo es: 15
"""

base = float(input("Base:"))
altura = float(input("Altura: "))

area = base * altura 
print(f"El area del rectangulo es : {area}")

"""4.	Calculadora simple
Pide al usuario dos números y muestra la suma, resta, multiplicación y división de esos números.
Ejemplo:
Entrada:
Primer número: 8
Segundo número: 4
Salida:
Suma: 12
Resta: 4
Multiplicación: 32
División: 2
"""

num1 = float(input("primer numero:"))
num2 = float(input("segunto numero:"))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"suma: {suma}, resta: {resta}, multiplicacion: {multiplicacion}, division: {division}")

"""5.	Cálculo del IVA
Pide al usuario el precio de un producto y calcula el precio final con un IVA del 19%.
Ejemplo:
Entrada:
Introduce el precio del producto: 100
Salida:
El precio final con IVA es: $119
"""

precio = float(input("introduce el precio del producto: "))
tasa_iva = float(input("Introduce la tasa de IVA (en decimal, por ejemplo, 0.19 para 19%): "))
precio_final = precio * (1 + tasa_iva)

print(f"El precio final con IVA es: ${precio_final:.2f}")


"""6.	Promedio de tres números
Solicita tres números al usuario y muestra su promedio.
Ejemplo:
Entrada:
Número 1: 5
Número 2: 7
Número 3: 10
Salida:
El promedio es: 7.33
"""
numero1 = float(input("Ingresar numero 1: "))
numero2 = float(input("Ingresar numero 2: "))
numero3 = float(input("Ingresar numero 3: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio es: {promedio}")

"""7.	Tiempo en segundos
Pide al usuario una cantidad de horas, minutos y segundos, y calcula el tiempo total en segundos.
Ejemplo:
Entrada:
Horas: 1
Minutos: 15
Segundos: 30
Salida:
El tiempo total es: 4530 segundos
"""
horas = int(input("Horas: "))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))

segundos_total = (horas * 3600) + (minutos * 60) + segundos
print(f"El tiempo total es: {segundos_total} segundos")