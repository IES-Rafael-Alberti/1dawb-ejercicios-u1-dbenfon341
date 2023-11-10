# Ejercicio 2.13
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", 
# donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.


n = int(input("Escribe un número: "))                                               #Pide al usuario un valor que se guarda en una variable.
m = int(input("Escribe otro número: "))                                             #Pide al usuario otro valor que se guarda en una variable.
c =  n // m                                                                         #Divide la variable n entre m sin decimales.
r = n % m                                                                           #Guarda el resto de la división en la variable r.

print ("La división entre", n ,"y", m ,"da un cociente", c ,"y un resto", r,".")    #Muestra el resultado pedido en el enunciado en consola.