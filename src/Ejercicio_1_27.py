# Ejercicio 2.27
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena 
# con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


producto = input("Introduce el nombre del producto: ")        #Crea una variable con el valor introducido por el usuario.
precio = float(input("Introduce su precio: "))                #Crea una variable con el valor introducido por el usuario.
unidades = int(input("Introduce las unidades: "))             #Crea una variable con el valor introducido por el usuario.
total = unidades * precio                                     #Crea la variable total, multiplicando las unidades por su precio.

#Muestra en pantalla el nombre del producto, el precio unitario con 6 digitos enteros y decimales (09.2f, siendo 9 el total mas el punto y las dos decimas y 2f las dos decimales),
#el número de unidades de tres dígitos y el total, de 8 digitos enteros y 2 decimales (11 en total sumando el punto y los dos decimales).

print (f"Nombre del producto: {producto} \nPrecio unitario: {precio:09.2f} \nNúmero de unidades: {unidades:03d} \nCoste total: {total:011.2f}")