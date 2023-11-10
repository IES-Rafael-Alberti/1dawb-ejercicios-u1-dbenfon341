# Ejercicio 2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
# Recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.


def calculo_iva(articulo, iva):
    ivaaplicado = (iva / 100) * (1 + articulo)
    total = articulo + ivaaplicado
    print (f"El artículo de coste {articulo} con el IVA aplicado ({iva}%) es: {total}€")
    return



calculo_iva(int(input("Introduce el coste total del artículo: ")),int(input("Introduce el IVA a aplicar:")))