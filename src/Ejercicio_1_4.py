# Ejercicio 2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.


temperatura = int(input("Introduce la temperatura Celsius para que pueda pasarla a Fahrenheit: "))      #Pide al usuario temperatura y la gurda en una variable
temperatura = ((temperatura*9/5)+32)                                                                    #Actualiza la variable con la formula de pasar Celsius a Fahrenheit.
print("La temperatura en Fahrenheit es:", temperatura)                                                  #Muestra la variable actualizada en un output.