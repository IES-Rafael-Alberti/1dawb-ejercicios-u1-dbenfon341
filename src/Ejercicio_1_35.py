#	
# Ejercicio 1.35 - Pide dos n�meros. Despu�s pide un tercer n�mero del 1 al 4, dependiendo de este n�mero el algoritmo debe hacer lo siguiente:
#	
#	- Si no es un n�mero correcto, escribir un mensaje de error.
#	- Si es un 1, escribir la suma de los dos primeros n�meros.
#	- Si es un 2, escribir la resta de los dos primeros n�meros.
#	- Si es un 3, escribir la multiplicaci�n de los dos primeros n�meros.
#	- Si es un 4, escribir la divisi�n de los dos primeros n�meros, siempre que el segundo no sea un 0. Si el segundo n�mero es un 0 escribe un mensaje de error "divisi�n por cero no es posible".
	
# > Introduce dos n�meros:
# > 5
# > 7
# > Introduce una opci�n (1 = Suma / 2 = Resta / 3 = Multiplicaci�n / 4 = Divisi�n): 3
# > 5 * 7 = 35
# 
# > Introduce dos n�meros:
# > 8
# > 0
# > Introduce una opci�n (1 = Suma / 2 = Resta / 3 = Multiplicaci�n / 4 = Divisi�n): 4
# > La divisi�n por cero no es posible
# 
# Inicio
# 
# 	Escribe "Introduce dos n�meros: "
# 	Lee n1
# 	Lee n2
# 	
# 	opcion = 0
# 	Mientras (opcion < 1 or opcion > 4) hacer
# 		Escribe "Introduce una opci�n (1 = Suma / 2 = Resta / 3 = Multiplicaci�n / 4 = Divisi�n): "
# 		Lee opcion
# 		Si (opcion < 1 or opcion > 4) entonces
# 			Escribe "Error - No es una opci�n correcta (1-4)"
# 	
# 	Segun (opcion) entonces
# 		1:
# 			Escribe n1 + " + " + n2 + " = " + (n1+n2)
# 		2:
# 			Escribe n1 + " - " + n2 + " = " + (n1-n2)
# 		3:
# 			Escribe n1 + " * " + n2 + " = " + (n1*n2)
# 		4:
# 			Si (n2 == 0) entonces
# 				Escribe "La divisi�n por cero no es posible"
# 			Sino
# 				Escribe n1 + " / " + n2 + " = " + (n1/n2)
# 	
# Fin

print ("Introduce dos números: ")
n1 = int(input())
n2 = int(input())

opcion = 0
while opcion < 1 or opcion > 4:
    opcion = int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "))

if (opcion < 1 or opcion > 4):
    print ("Error - no es una opción correcta (1-4)")
elif opcion == 1:
    print (n1, "+", n2, "=", n1+n2)
elif opcion == 2:
    print (n1, "-", n2, "=", n1-n2)
elif opcion == 3:
    print (n1, "*", n2, "=", n1*n2)
elif opcion == 4:
    if (n2 == 0):
        print("La división por cero no es posible.")
    else:
        print(n1, "/", n2, "=", n1/n2)