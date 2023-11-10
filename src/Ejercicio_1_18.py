# Ejercicio 2.18
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y 
# otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.


nombre = input("Introduce tu nombre con apellidos: ")                       #Crea la variable nombre con el valor que introduzca el usuario. (nombre completo)

print("Nombre en minúsculas:", nombre.lower())                              #Muestra en terminal la variable introducida, pero con todas las letras en minúsculas.
print("Nombre en mayúsculas:", nombre.upper())                              #Muestra en terminal la variable introducida, pero con todas las letras en mayúsculas.
print("Nombre con las primeras letras en mayúscula:", nombre.title())       #Muestra en la terminal la variable introducida, pero con la primera letra de cada palabra en mayúsculas.