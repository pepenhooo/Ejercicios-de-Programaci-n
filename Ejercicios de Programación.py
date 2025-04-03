import math
import sys
#Problema 1
print("Hola, ya se imprimir frases.")

#Problema 2
print("279")

#Problema 3
print("5.1")

#Problema 4
print(1234+532)

#Problema 5
print(1234-532)

#Problema 6
print(1234*532)

#Problema 7
print(1234/532)

#Problema 8
for i in range(1, 4):
    print(i)

#Problema 9
i = 1
while i < 10:
    print(i)
    i += 1

#Problema 10
i = 1
while True:
    print(i)
    i += 1

#Problema 11
def print_numbers(start, end):
    print(start)
    if start < end:
        print_numbers(start + 1, end)
    if start == end:
        return

#Problema 12
numbers = list(range(5, 16))
print(*numbers, sep="\n")

#Problema 13
for num in range(5, 15001):
    print(num)

#Problema 14
print("hola\n" * 200, end="")

#Problema 15
for num in range(1, 31):
    print(num ** 2)

#Problema 16
for num in range(1,21):
    print(math.factorial(num))

#Problema 17
numeros = []
for num in range(1, 101):
    numeros.append(num ** 2)
print(sum(numeros))

#Problema 18
numero = int(input("Ingrese un número entero: "))
suma = sum(range(numero + 1, numero + 101))
print("La suma da", suma)

#Problema 19
euro = int(input("Ingrese la cantidad de euros: "))
dolar = euro *1.11
print("Tienes ", dolar, "dólares")

#Problema 20
alto = float(input("Cuál es la altura de su rectángulo?: "))
ancho = float(input("Cuál es el ancho de su rectángulo?: "))
area = alto * ancho
print("El área del rectángulo es:", area)

#Problema 21
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"El mayor es {num1} y el menor es {num2}")
elif num1 < num2:
    print(f"El mayor es {num2} y el menor es {num1}")
else:
    print("Los números son iguales")

#Problema 22
num = int(input("Ingrese un número: "))
for i in range(1, num):
    if i % 2 != 0:
        print(i)

#Problema 23
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"El GCD de {num1} y {num2} es: {gcd(num1, num2)}")

#Problema 24
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    root1 = (-b + math.sqrt(discriminante)) / (2 * a)
    root2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print(f"Las soluciones son: {root1} y {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"La solución única es: {root}")
else:
    print("La ecuación no tiene soluciones reales.")

#Problema 25
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

    # Ackermann function using recursion
def ackermann(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ackermann(x - 1, 1)
    else:
        return ackermann(x - 1, ackermann(x, y - 1))

    # Test the functions
n = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {n} es: {factorial(n)}")

x = int(input("Ingrese el valor de x para la función de Ackermann: "))
y = int(input("Ingrese el valor de y para la función de Ackermann: "))
print(f"Ackermann({x}, {y}) = {ackermann(x, y)}")

#Problema 26
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)

print(f"El menor de los números es: {menor}")
print(f"El mayor de los números es: {mayor}")

#Problema 27
while True:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit (999 para salir): "))
    if fahrenheit == 999:
        break
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"La temperatura en grados Celsius es: {celsius:.2f}")

#Problema 28
for i in range(1, 5):
    match i:
        case 1:
            print("Caso 1: Hola")
            break
        case 2:
            print("Caso 2: Adiós")
            break
        case 3:
            print("Caso 3: Bienvenido")
            break
        case 4:
            print("Caso 4: Hasta luego")
            break

for i in range(1, 5):
    match i:
        case 1:
            print("Caso 1: Hola")
        case 2:
            print("Caso 2: Adiós")
        case 3:
            print("Caso 3: Bienvenido")
        case 4:
            print("Caso 4: Hasta luego")
