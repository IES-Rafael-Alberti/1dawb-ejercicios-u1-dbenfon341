# Ejercicio 2.2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.


horas = int(input("Horas de trabajo: "))            #Crea variable horas con el input del usuario.
precio = int(input("Coste por hora: "))             #Crea variable precio con el input del usuario.
total = horas * precio                              #Crea la variable total con la multiplicación de horas y precio.

print("Importe total:", total)                      #Imprime el resultado.