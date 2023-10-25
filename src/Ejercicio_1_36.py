#	
# Ejercicio 1.36 - Calcula la media de las notas de un curso.
# P�de el n�mero de notas que va a introducir al principio.
# El n�mero de notas no puede ser un n�mero superior a 100, o inferior a 1.
# Si no introduce un n�mero de notas correcto escribimos el mensaje "Error - el n�mero de notas debe ser un n�mero entero entre 1 y 100"
#
#
#> �Cu�ntas notas vas a introducir? 0
#> Error - el n�mero de notas debe ser un n�mero entero entre 1 y 100
#> �Cu�ntas notas vas a introducir? 187
#> Error - el n�mero de notas debe ser un n�mero entero entre 1 y 100
#> �Cu�ntas notas vas a introducir? 3
#> Dame las 3 notas del curso:
#> 9
#> 7.5
#> 10
#> La media es 8.83
#	
#Inicio
#
#	Escribe "�Cu�ntas notas vas a introducir? "
#	Lee total
#	
#	Mientras (total < 1 o total > 100) hacer
#		Escribe "Error - el n�mero de notas debe ser un n�mero entero entre 1 y 100"
#		Escribe "�Cu�ntas notas vas a introducir? "
#		Lee total
#
#	Escribe "Dame las " + total + " notas del curso: "
#	
#	media = 0
#	cont = 1
#	Mientras (cont <= 10) hacer
#		Lee nota
#		media = media + nota
#		cont = cont + 1
#
#	media = media / total
#	Escribe "La media es " + media
#	
#Fin

total = int(input("¿Cuántas notas vas a introducir? "))

while total < 1 or total > 100:
    print("Error, el número de notas debe ser un número entero entre 1 y 100")
    total = int(input("¿Cuántas notas vas a introducir? "))

print ("Dame las", total ," notas del curso: ")

media = 0
cont = 1

while (cont <= total):
    nota = float(input())
    media = media + nota
    cont = cont + 1

media = media / total
print ("La media es", round(media, 2))