# Ejercicio 2.6
# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).


precioarticulo = int(input("Indique el importe final del artículo: "))                                  #Input que pide al usuario introducir el importe del artículo.
iva = precioarticulo / 1.10                                                                             #Divide el precio del artículo entre 1.10 para sacar el 10% del iva del precio.
print("Su artículo sin IVA cuesta:", iva ,"\nHa pagado un total de IVA de:", precioarticulo - iva)      #Se le resta al precio final.