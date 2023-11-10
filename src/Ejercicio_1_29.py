#Ejercicio 1.29
#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
#El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


# Inicio
# 
#     Escribe "Introduce tu nombre: "
#     Lee nombre
#     Si nombre == "" entonces
#       nombre = "Desconocido"
# 
#     Escribe "Introduce tu edad: "
#     Lee edad
#     Mientras edad (<= 0 or edad >= 125) hacer
#       Escribe "Introduce una edad válida: "
#       Lee edad
# 
#     Escribe "Te llamas" + nombre + "y tienes" + edad + "años, te quedan aún" + (125 - edad) + "años por cumplir."
# 
# Fin


nombre = input("Introduce tu nombre: ")                 #Crea la variable nombre, con el valor que proporcione el usuario
if nombre == (""):                                      #Si el valor que proporciona el usuario está vacío entonces:
    nombre = ("Desconocido")                            #Actualiza la variable nombre con el valor "Desconocido".

edad = int(input("Introduce tu edad: "))                #Crea la variable "edad" con el valor introducido por el usuario.

while edad <= 0 or edad >= 125:                         #Se crea un bucle en el que si la edad introducida es menor o igual a 0 o mayor o igual a 125 entonces:
    edad = int(input("Introduce una edad válida: "))    #Vuelve a pedir una edad nueva para actualizar la variable edad, hasta que entre en un valor comprendido entre 0 y 125.

print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir.")     #Muestra el resultado, restandole 125 a la edad.