# Ejercicio 2.8
# Escribir el programa del ejercicio 7 usando solamente dos variables diferentes.


resultado = 0                                               #Se crea la variable resultado con valor 0.
for i in range(0,3 + 1):                                    #Bucle for que da tres vueltas por el rango 0, 3.
    numero = int(input("Introduce un número: "))            #Introduce un input en cada vuelta del bucle.
    print(i)
    resultado += numero                                     #Resultado pasa a ser 0 + el número que se incluya en el input en cada pase del bucle.
    
print("La suma total de los tres números es:", resultado)   #Muestra en consola el resultado final (resultado = a la vuelta del bucle 3 veces)