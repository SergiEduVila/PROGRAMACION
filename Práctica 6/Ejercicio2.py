#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 2#

#Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.#
#Escribe un nombre: 14#
#Escribe una otro nombre: 123#
#Escribe una otro nombre: -25#
#Escribe una otro nombre: 123#
#Escribe una otro nombre: Salir#
#Los números que has escrito son [14, 123, -25, 123]#


print("Introduce un número:")
num=input()
lnum=[]
trap=int(num)
lnum.append(trap)
while num != "Salir" and num !="salir":
    print("Introduce otro número:")
    num=input()
    if num != "Salir" and num != "salir":
        trap=int(num)
        lnum.append(trap)
    
print("Los números que has escrito són: ", lnum)
