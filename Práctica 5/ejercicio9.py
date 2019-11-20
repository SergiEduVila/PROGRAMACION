#Sergi Vila Sánchez Eduard# #Práctica 6 Ejercicio 9#

#Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:#
#Anchura del rectángulo: 5#
#Altura del rectángulo: 4#
#*****#
#*   *#
#*   *#
#*****#

print("Introduce la anchura del rectángulo:")
ancho=int(input())
print("Introduce la altura del rectángulo:")
altura=int(input())

#FORMA 1#
for i in range(1, altura + 1):
    for j in range(1, ancho + 1):
        if i == 1 or i==altura or j==1 or j==ancho:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(" ")


#FORMA 2#
for i in range(altura):
    if i == 0 or i == altura-1:
        print("*"*ancho)
    else:
        print("*"+" " * (ancho-2) + "*")
