## +
def suma(num1, num2):
    return num1 + num2
##  -
def resta(num1, num2):
    return num1 - num2
##  *
def multipicacion(num1, num2):
    return num1 * num2

##  %/
def division(num1, num2):
    if num2 == 0:
        return "Error: Division por cero"
    else:
        return num1 / num2 

def modulo(num1, num2):
    return num1 % num2

operacion = input("Ingrese la operacion ( +, -, *, /): ")
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if operacion == '+':
    resultado = suma(num1, num2)
elif operacion == '-':
    resultado = resta(num1, num2)
elif operacion == '*':
    resultado = multipicacion(num1, num2)
elif operacion == '/':
    resultado = division(num1, num2)
else:
    print("operacion no valida")

print(f"El resultado es: {resultado}")
