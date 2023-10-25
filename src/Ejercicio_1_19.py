# Ejercicio 2.19
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", 
# donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.


nombre = input("Introduce tu nombre: ")                             #Crea la variable nombre con el valor que introduzca el usuario.
print(nombre,"tiene",len(nombre),"letras.")                         #Muestra en pantalla la variable nombre, y con len se muestra el número de letras que tiene dicha palabra.