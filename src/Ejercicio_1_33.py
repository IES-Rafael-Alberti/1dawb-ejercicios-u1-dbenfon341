#
# Ejercicio 1.33 - Lee 3 n�meros y dame los n�meros ordenados de menor a mayor.
#

# > Dame 3 n�meros:
# > 14
# > 7
# > 10
# > Tus n�meros son 7 10 14
# 
# Inicio
# 
# 	Escribe "Dame 3 n�meros: "
# 	Lee n1
# 	Lee n2
# 	Lee n3
# 	
# 	Si (n1 < n2 and n1 < n3) entonces
# 		Si (n2 < n3) entonces
# 			Escribe n1 + " " + n2 + " " + n3
# 		Sino
# 			Escribe n1 + " " + n3 + " " + n2
# 	Sino
# 		Si (n2 < n1 and n2 < n3) entonces
# 			Si (n1 < n3) entonces
# 				Escribe n2 + " " + n1 + " " + n3
# 			Sino
# 				Escribe n2 + " " + n3 + " " + n1
# 		Sino
# 			Si (n3 < n1 and n3 < n2) entonces
# 				Si (n1 < n2) entonces
# 					Escribe n3 + " " + n1 + " " + n2
# 				Sino
# 					Escribe n3 + " " + n2 + " " + n1
# 
# Fin


print ("Dame tres números: ")                           #Pide tres valores para las variables n1, n2 y n3.
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 < n2 and n1 < n3:                                 
    if n2 < n3:
        print("Tus números son:", n1, n2, n3)
    else:
        print("Tus números son:", n1, n3, n2)
elif n2 < n1 and n2 < n3:
    if n1 < n3:
        print("Tus números son:", n2, n1, n3)
    else:
        print("Tus números son:", n2, n3, n1)
else:
    if n3 < n1 and n3 < n2:
        if n1 < n2:
            print("Tus números son:", n3, n1, n2)
        else:
            print("Tus números son:", n3, n2, n1)