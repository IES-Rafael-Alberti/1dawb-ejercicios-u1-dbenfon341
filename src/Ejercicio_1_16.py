# Ejercicio 2.16
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan 
# (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.


panes = int(input("Introduce la cantidad de barras de pan vendido que no es del día: "))            #Pide input al usuario y guarda el valor en la variable panes.
precio = 3.49                                                                                       #Crea la variable precio con el valor 3.49
coste = (panes * precio) * (1 - 0.6)                                                                #Crea la variable coste, multiplicando panes por el precio y multiplicandolo por 1 - 06.

print("El coste de las barras de pan frescas es de", precio ,"€.\nEl descuento del pan que no es del dia es del 60%.\nEl coste total a pagar es:", round(coste, 2) ,"€.")