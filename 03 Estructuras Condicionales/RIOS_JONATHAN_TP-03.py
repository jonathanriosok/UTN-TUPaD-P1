#Programa mayoria de edad
#Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))
#Verificar si el usuario es mayor de 18 años
if edad > 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")


#Programa nota
#Solicitar la nota al usuario
nota = float(input("Por favor, ingresa tu nota: "))
#Verificar si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")

#Programa numero pares
#Solicitar un numero al usuario
numero = int(input("Por favor, ingrese un numero: "))
#Verificar si el numero es par utilizando el operador de modulo (%)
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Programa que edad tienes
#Solicitar la edad al usuario
edad = int(input("Por favor, ingrese su edad: "))
#Determinar la categoria segun la edad
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Validador de contraseña
#Solicitar una contraseña al usuario
contraseña = input("Por favor, ingrese una contraseña: ")
#Verificar si la longitud de la contraseña es adecuada (entre 8 y 14 caracteres)
if 8<= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Programa con Stactistics
import random
from statistics import mode, median, mean
#Crear la lista de numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Calcular la moda, la mediana, la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
#Determinar el tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo o a la derecha.")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda.")
elif media == mediana == moda:
    print("Sin sesgo.")
else:
    print("La distribucion no cumple con las condiciones para determinar el sesgo.")
#Mostrar los resultados calculados
print(f"Lista de numeros:{numeros_aleatorios}")
print(f"Media:{media}")
print(f"Mediana:{mediana}")
print(f"Moda:{moda}")

#Frases
#Solicitar una frase o palabra al usuario
texto = input("Por favor, ingrese una frase o palabra: ")
#Lista de vocales 
vocales = "aeiouAEIOU"
#Verificar si el ultimo caracter del string es una vocal
if texto[-1] in vocales:
    texto_modificado = texto + "!"
else: 
    texto_modificado = texto
#Imprimir el resultado
print("Resultado:", texto_modificado)

#Transformador de nombres
#Socilitar el nombre al usuario
nombre = input("Por favor, ingrese su nombre: ")
#Solicitar la opcion al usuario
print("Seleccione una opcion:")
print("1. Convertir el nombre a mayusculas.")
print("2. Corvertir el nombre a minusculas.")
print("3. Convertir el nombre con la primera letra en mayuscula.")
opcion = int(input("Ingrese el numero de la opcion deseada (1,2 o 3): "))
#Transformar el nombre segun la opcion seleccionada
if opcion == 1:
    print("Resultado", nombre.upper())
elif opcion == 2:
    print("Resultado", nombre.lower())
elif opcion == 3: 
    print("Resultado", nombre.title())
else:
    print("Opcion no valida. Por favor, ingrese 1, 2 o 3.")

#Calificar terremoto
#Solicitar la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto (segun escala de Richter): "))
#Clasificar la magnitud segun la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (Ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles).")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
else: #magnitud >= 7 
    print("Extremo (puede causar graves daños a gran escala).")

#Estaciones del año
#Solicitar ña informacion al usuario
hemisferio = input("Por favor, ingrese el hemisferio en el que se encuentre (N/S):").strip().upper()
mes = input ("Ingrese el mes actual (en minusculas, por ejemplo: enero febrero, etc.):").strip().lower()
dia = int(input("Ingrese el dia del mes actual (1-31): "))
#Definir las estaciones segun el hemisferio y la fecha
if hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero","febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Verano"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
            estacion = "Verano"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
            estacion = "Otoño"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
            estacion = "Invierno"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
            estacion = "Primavera"
else:
    estacion = None
#Imprimir el resultado 
if estacion:
    print(f"Actualmente te encuentra en la estacion: {estacion}")
else: 
    print("Hemisferio no valido. Por favor, ingrese 'N' para el hemisferio norte o 'S' para el hemisferio sur.")