"""
1.	Generar una lista de números
"""

num = int(input("Ingresa numero: "))

tomaValorNum = num

while tomaValorNum > 0:
    print(tomaValorNum)
    tomaValorNum -= 1

"""2.	Sumar elementos de una lista"""

numero = input("Ingrese los numeros que quiera sumar, separados por coma ',': ")

listNumero = list(map(int, numero.split(',')))

suma = 0

for numero in listNumero:
    suma += numero
print("la cantidad final segun el valor ingresado es: ", suma)

"""3.	Filtrar números pares
Solicita una lista de números al usuario y usa un bucle for para agregar solo los números pares a una nueva lista.
Ejemplo:
Entrada: [1, 2, 3, 4, 5, 6]
Salida: [2, 4, 6]"""

numIngresados = input("Ingrese los numeros separados por coma ',': ")

numLista = list(map(int, numIngresados.split(',')))

numPar = []

for num in numLista:
    if num % 2 == 0:
       numPar.append(num)

print("Segun los nunmeros ingresados, los numero que son pares son: ", numPar)

"""4.	Cálculo del promedio y evaluación
Escribe un programa que permita al usuario ingresar números (notas) hasta que escriba la palabra "fin". El programa debe calcular el promedio de las notas ingresadas. Usa un bucle while para obtener las notas y una condicional para determinar si el promedio indica que el usuario aprobó o reprobó.

Condiciones:
Si el promedio es mayor o igual a 4.0, el usuario aprueba.
Si es menor a 4.0, el usuario reprueba.
Ejemplo:

Entrada: 5, 3, 4, fin

Salida:
El promedio es: 4.0
¡Aprobaste!

Entrada: 2, 3, fin

Salida:
El promedio es: 2.5
Reprobaste.
"""


notas = []  
suma_notas = 0 
contador_notas = 0  

while True:
    nota = input("Ingrese una nota (o 'fin' para terminar): ")
    if nota == "fin":
        break  
    else:
        nota = float(nota)  
        notas.append(nota)  
        suma_notas += nota  
        contador_notas += 1  

if contador_notas > 0:  
    promedio = suma_notas / contador_notas
    print(f"El promedio es: {promedio:.1f}")
    if promedio >= 4.0:
        print("¡Aprobaste!")
    elif promedio <= 4.0:
        print("Reprobaste.")
    else:
     print("No se ingresaron notas.")



## dios mio 
