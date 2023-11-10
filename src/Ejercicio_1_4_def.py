# Ejercicio 2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
# NO recibe parámetros y retorna la temperatura convertida en grados Celsius. Dentro de la función se pedirá al usuario los grados Farenheit.


def fahrenheit():
    temperatura = int(input("Introduce la temperatura Fahrenheit para que pueda pasarla a Celsius: "))
    celsius = (temperatura - 32) * 5/9
    return celsius

print (f"La temperatura en Celsius es {round(fahrenheit(), 2)}ºC")