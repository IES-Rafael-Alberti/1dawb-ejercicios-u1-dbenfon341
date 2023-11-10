# Ejercicio 2.17
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla 
# en líneas distintas el nombre del usuario tantas veces como el número introducido.


nom = str(input("Escribe tu nombre de usuario: "))          #Crea una variable string con el nombre nom.
num = int(input("Escribe otro número: "))                   #Crea una variable numero entero llamada num.

i = 0                                                       #Se crea una variable llamada i que empieza en 0 que hace como contador.
while i < num:                                              #Mientras el contador (que empieza en 0) sea menor que la variable numero:
    print (nom)                                             #imprime la variable nom
    i += 1                                                  #Suma +1 a la variable i (la que hace de contador). Cuando la variable llegue a ser mayor que num, parará.