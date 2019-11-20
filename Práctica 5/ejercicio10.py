#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 10#

#Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:#
#Altura de un triángulo: 5#
#    *    #
#   ***   #
#  *****  #
# ******* #
#*********#


print("Introduce la altura del triángulo:")
altura=int(input())

for i in range(1, altura+1):
        print((" "*(altura-i))+("*"*(i-1))+("*"*i)+(" "*(altura-i)))
