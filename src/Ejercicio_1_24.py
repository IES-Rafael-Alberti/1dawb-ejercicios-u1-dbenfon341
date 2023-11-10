# Ejercicio 2.24
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.


dinero = input("¿Cuanto cuesta el producto? Introduce el precio con dos decimales: ") #Pide al usuario introducir un numero con dos decimales y los almacena en la variable "dinero".

dinerodividido = dinero.split(".")                                                    #Divide la cantidad a partir del simbolo ".".
euros = dinerodividido[0]                                                             #Guarda en la variable euros lo que está delante del ".".
centimos = dinerodividido[1]                                                          #Guarda en la variable centimos lo que está detrás del ".".

print(f"El precio es de{euros} euros y {centimos} céntimos.")                         #Muestra en pantalla el mensaje junto a las variables euros y centimos.





#Pide el dinero total de un producto con dos decimales.
#dinero = input("¿Cuanto cuesta el producto? Introduce el precio con dos decimales: ")
#Muestra en la pantalla la variable dinero, busca el . y borra lo que hay detrás. con : . En los céntimos hace lo mismo pero borrando lo que hay delante mas el punto.
#print(f"{dinero[:dinero.find('.')]} euros y {dinero[dinero.find('.')+1:]} céntimos.")