# Ejercicio 2.12
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.


peso = int(input("Introduce tu peso (en kg): "))                #Pide al usuario introducir su peso y lo guarda en una variable.
altura = float(input("Introduce tu estatura (en metros): "))    #Pide al usuario introducir su altura y lo guarda en una variable con decimales.
masacorporal = peso / (altura**2)                               #Se aplica la formula para calcular el IMC (peso / (altura**2) y se añade a una variable.

print("Tu indice de masa corporal es:", round(masacorporal, 2)) #Muestra en consola el resultado final.