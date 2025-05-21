#1 Programa que imprime todos los numeros enteros desde 0 hasta 100, uno por linea.

for numero in range (0, 101):
    print(numero)



#2 Programa que solicita un numero entero al usuario y muestra la cantidad de digitos que contiene

numero = input("Introduce un numero entero: ")

#Maneja numeros negativos eliminando el signo
if numero.startswith ('-'):
    numero = numero [1:]

cantidad_digitos = len(numero)
print("Cantidad de digitos:", cantidad_digitos)

#3 Programa que suma todos los numeros enteros comprendidos entre dos valores por el usuario(Excluyendo los extremos)

#Solicitar los valores al usuario
inicio = int(input("Introduce el primer valor entero: "))
fin = int(input("Introduce el segundo valor entero: "))

#Determinar los limites inferior y superior
limite_inferior = min(inicio, fin) +1
limite_superior = max(inicio, fin)

#Calcular la suma excluyendo los extremos
suma = 0
for numero in range (limite_inferior, limite_superior):
    suma+= numero

print("La suma de los numeros enteros entre", inicio, "y", fin, "excluyendo ambos, es:", suma)

#4 Programa que suma números enteros ingresados por el usuario hasta que se ingrese un 0

numero = int(input("Introduce un numero entero (0 para terminar): "))
total = 0

while numero != 0:
    total += numero
    numero = int(input("Introduce un numero entero (0 para terminar): "))

print("La suma total es:", total)

#5 Juego donde tenes que adivinar un número aleatorio entre 0 y 9.

import random

numero_secreto = random.randint(0, 9)
intentos = 0
acertado = False

print("Adivina el numero entre 0 y 9.")

while not acertado:
    intento = int(input("Introduce tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        acertado = True
        print(f"Correcto! Adivinaste el numero en {intentos} intentos.")
    else:
        print("Incorrecto, intenta de nuevo.")

#6 Programa que imprime todos los números pares entre 0 y 100 en orden decreciente

for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

#7 Programa que calcula la suma de todos los numeros comprendidos entre 0 y un numero entero positivo dado por el usuario

n = int(input("Introduce un numero entero positivo: "))
suma = 0

for numero in range(0, n + 1):
    suma += numero

print("La suma de los numeros desde 0 hasta", n, "es:", suma)

#8 Programa que pide 100 numeros enteros y cuenta pares, impares, negativos y positivos

# Se puede cambiar este valor para pruebas rapidas
CANTIDAD_NUMEROS = 10

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
print("Cantidad de numeros positivos:", positivos)
print("Cantidad de numeros negativos:", negativos)

#9 Programa que permite al usuario ingresar 100 numeros enteros y calcula la media

CANTIDAD_NUMEROS = 10  # Cambia este valor para probar con menos numeros

suma = 0

for i in range(CANTIDAD_NUMEROS):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma += numero

media = suma / CANTIDAD_NUMEROS
print("La media de los numeros ingresados es:", media)

#10 Programa que invierte el orden de los dígitos de un número ingresado por el usuario

numero = input("Introduce un número: ")

# Si el número es negativo, se maneja el signo por separado
if numero.startswith('-'):
    invertido = '-' + numero[:0:-1]
else:
    invertido = numero[::-1]

print("El número invertido es:", invertido)