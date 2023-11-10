# Ejercicio 2.23
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
# pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.


correo = input("Introduce tu correo electrónico: ")                 #Pide al usuario el un input para guardar en la variable "correo".
parteanterior = correo.split("@")[0]                                #Crea una variable nueva con correo, pero esta vez utiliza split para borrar lo que hay a partir del simbolo @.
nuevocorreo = parteanterior + "@ceu.es"                             #Crea la variable nuevocorreo con valor de suma de la variable parteanterior con @ceu.es.

print("Tu correo con el nuevo dominio es:", nuevocorreo)            #Muestra en consola el resultado final.