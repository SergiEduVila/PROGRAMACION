#Sergi Eduard Vila Sánchez# #Práctica 5 Ejercicio 11#

#Escribe un programa que pida un número e imprima todos sus divisores.#
#Dame un número: 200#
#Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200#


print("Introduce un número cualquiera:")
num=int(input())

print("Los divisores de ", num, "son: ")
for i in range(1, num+1):
    resto=num%i
    if resto==0:
        print(i, end=" ")
print(" ")
