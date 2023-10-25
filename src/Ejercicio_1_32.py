#
# Ejercicio 1.32 - Lee dos n�meros y crea la serie que los une de 1 en 1...
#
#
#> Introduce un n�mero: 4
#> Introduce otro: 8
#> 4-5-6-7-8
#
#> Introduce un n�mero: 12
#> Introduce otro: 3
#> 3-4-5-6-7-8-9-10-11-12
#
#Inicio
#
#	Escribe "Introduce un n�mero: "
#	Lee x
#	Escribe "Introduce otro: "
#	Lee y
#	
#	Si (x >= y) entonces
#		numIni = x - 1
#		numFin = y
#	Sino
#		numIni = y - 1
#		numFin = x
#		
#	Para i en (numIni...numFin) hacer
#		Escribe i + 
#		Si (numIni != numFin) entonces
#			Escribe "-"
#
#Fin


x = int(input("Introduce un número: "))         #Pide un número al usuario y guarda su valor en la variable x.
y = int(input("Introduce otro: "))              #Pide un número al usuario y guarda su valor en la variable y.

if x >= y:                                      #Si x es mayor o igual que y:
    numIni = y                                  #La variable NumIni es igual a y.
    numFin = x                                  #y la variable NumFin toma el valor de la variable x.
else:                                           #Si no...
    numIni = x                                  #La variable numIni toma el valor de x
    numFin = y                                  #Y la variable numFin toma el valor de la variable y.


#En este bucle for, el rango es desde la variable numIni hasta la variable numFin.
#Imprime i (el numero numIni) en pantalla y sigue la linea.
#Después con el if, verifica si i es diferente a numFin, y en caso de serlo imprime un "-".

for i in range(numIni, numFin +1):
    print(i, end="")
    if i != numFin:
        print("-", end="")