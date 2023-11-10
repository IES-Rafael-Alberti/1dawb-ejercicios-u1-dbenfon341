# Ejercicio 2.11
# Escribir un programa que lea un entero positivo, n, introducido por el usuario y 
# después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
# suma = n(n+1) / 2
# Recibe un número y retorna una cadena de caracteres con el resultado de la función.


def calculo(num1):
    num2 = num1 * (num1+1) // 2
    return print(f"El número es: {num2}")


calculo(int(input("Introduce un número: ")))
