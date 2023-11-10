# Ejercicio 2.25
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
# Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.


fecha = input("Introduce tu fecha de nacimiento con el formato dd/mm/aaaa: ") #Crea la variable fecha con el valor introducido, debe ser xx/xx/xxxx.
fechadividida = fecha.split("/")                                              #Divide la variable en tres listas cada vez que lee /.
dia = fechadividida[0]                                                        #Crea una variable dia, con la primera parte dividida de la lista con /.
mes = fechadividida[1]                                                        #Crea una variable mes, con la segunda parte dividida de la lista con /.
año = fechadividida[2]                                                        #Crea una variable año, con la tercera parte dividida de la lista con /.
print(f"Su fecha de nacimiento es: {dia} / {mes} / {año}")                    #Muestra el resultado en pantalla.