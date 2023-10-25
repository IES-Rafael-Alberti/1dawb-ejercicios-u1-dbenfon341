# Ejercicio 2.14
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística 
# les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


payaso = 112                                                                    #Variable payaso con valor 112.
muñeca = 75                                                                     #Variable muñeca con valor 75.

totalpayaso = int(input("¿Cuantas payasos se vendieron?: "))                    #Crea la variable totalpayaso con el valor introducido por el usuario.
totalmuñeca = int(input("¿Y muñecas?: "))                                       #Crea la variable totalmuñeca con el valor introducido por el usuario.

totalpayaso = payaso * totalpayaso                                              #Actualiza la variable totalpayaso con la multiplicacion de payaso y totalpayaso.
totalmuñeca = muñeca * totalmuñeca                                              #Actualiza la variable totalmuñeca con la multiplicación de muñeca y totalmuñeca.
pesototal = totalpayaso + totalmuñeca                                           #Crea la variable pesototal con la suma de las dos variables.

print ("El peso total del paquete es de ", pesototal ," gramos.")               #Muestra por pantalla el resultado final (la última variable).