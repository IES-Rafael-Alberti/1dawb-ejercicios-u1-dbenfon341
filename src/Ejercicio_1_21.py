# Ejercicio 2.21
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


frase = input("Introduce una frase: ")          #Pide a un usuario un input para introducir en la variable creada "frase".
frase = frase[::-1]                             #Invierte el contenido de la variable.
print(frase)                                    #Muestra la variable "frase" invertida.