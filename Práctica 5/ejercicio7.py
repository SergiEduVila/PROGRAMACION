#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 7#

#Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:#
#Altura del triángulo: 4#
#****#
#***#
#**#
#*#


print("Introduce la altura del triángulo:")
altura=int(input())

for i in range(altura,0,-1):
    print(i*("*"),end=(""))
    print("")
