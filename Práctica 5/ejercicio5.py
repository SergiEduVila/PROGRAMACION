#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 5#

#Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:#
#Anchura del rectángulo: 5#
#Altura del rectángulo: 3#
#*****#
#*****#
#*****#


print("Inserta el valor de la base del rectángulo:")
base=int(input())
print("Inserta ahora la altura:")
altura=int(input())

for i in range(base):
    for j in range(altura):
        print("*", end=(""))
    print("")

