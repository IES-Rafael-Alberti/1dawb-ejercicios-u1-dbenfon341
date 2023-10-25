# Ejercicio 2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n+1) / 2


numero = int(input("Introduce un número: "))                    #Pide un número al usuario.

if numero < 1:                                                  #Si el número es menor a 0, acaba el código.
    print("Por favor, introduce un número entero positivo.")    #Muestra error en la consola por introducir un número no entero.
else:                                                           #Si no, hace lo siguiente:
    numeros = numero * (numero+1) // 2                          #Aplicamos la fórmula que nos proporciona el enunciado, numero * (numero+1) / 2 y lo añade a la variable numero*S*.
    print(numeros)                                              #Nos da la variable numero*S* con la formula aplicada.