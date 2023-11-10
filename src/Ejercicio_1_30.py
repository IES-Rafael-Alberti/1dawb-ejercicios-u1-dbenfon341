#Ejercicios 1.30
#Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
#El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, 
#la primera opción es más fácil, aunque el mundo está lleno de valientes)
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
#El pseudocódigo debes incluirlo como comentarios en el programa de Python.


# Inicio
# 
#     Escribe "Introduce un número: "
#     Lee numero
#     Escribe "Introduce de cuanto en cuanto saltará el número: "
#     Lee incremento
# 
#     Si numero <= 0 entonces
#       Escribe "Has introducido un número incorrecto"
#     Sino
#       Si incremento <=0 entonces
#          Escribe "has introducido un incremento incorrecto. El número debe ser mayor que 0."
#       Sino
#          Escribe "¿En qué número debe parar la serie?: "
#          Lee serie
#          Escribe "SERIE =>" + numero
#          
#     Mientras (numero < serie) hacer
#       numero += incremento
#       Escribe "-" + numero
#      
# Fin


numero = int(input("Introduce un número: "))
incremento = int(input("Introduce de cuanto en cuanto saltará el número: "))
serie = 0

if numero <= 0:
    print("Has introducido un número incorrecto. El número debe ser mayor que 0.")
elif incremento <= 0:
    print("Has introducido un incremento incorrecto. El número debe ser mayor que 0.")
else:
    serie = int(input("¿En qué número debe parar la serie?: "))
    print(f"SERIE => {numero}", end="")

while numero < serie:
    numero = numero + incremento
    print(f"-{numero}", end="")