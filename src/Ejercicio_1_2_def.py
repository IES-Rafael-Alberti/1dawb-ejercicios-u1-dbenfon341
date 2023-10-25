# Ejercicio 2.2
# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
# Recibe horas y coste y retorna el importe total.


def total(horas, coste):
    return print(f"Importe total: {horas*coste}")


total(int(input("Horas de trabajo: ")), int(input("Coste por hora: ")))