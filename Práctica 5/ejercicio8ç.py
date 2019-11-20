#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 8#

#Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:#
#Altura del triángulo: 4#
#*#
#**#
#***#
#****#
#***#
#**#
#*#


print("Introduce la anchura que quieras para el triángulo:")
anchura=int(input())

for i in range(1, anchura+1):
    print(i*"*", end=" ")
    print(" ")
for i in range(anchura+1, 0, -1):
    print(i*"*", end=" ")
    print(" ")
