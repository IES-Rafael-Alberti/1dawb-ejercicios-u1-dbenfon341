# Ejercicio 2.20
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


num = input("Introduce un número de teléfono con el prefijo y la extensión de dos dígitos (por ejemplo: 3491372471056): ")      #Pide al usuario un número de telefono de una forma determinada.
num = num[+2:-2:]                                                                                                               #Resta a la variable num los dos primeros y ultimos digitos.
print("El número de teléfono sin prefijo y extensión es:", num)                                                                 #Imprime la variable num con la ultima modificación.