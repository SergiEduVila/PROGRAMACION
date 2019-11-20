#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 6#

#Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:#
#Altura del triángulo: 4#
#*#
#**#
#***#
#****#


print("Introduce la altura del triángulo:")
altura=int(input())

for i in range(1, altura+1):
    for j in range(+i):
        print("*", end="")
    print("")
