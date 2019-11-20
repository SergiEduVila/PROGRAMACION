#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 4#

#Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. El programa termina escribiendo los dos números tal y como se pide:#
#Escribe un número: 6#
#Escribe un número mayor que 6: 6#
#6 no es mayor que 6. Vuelve a introducir un número: 1#
#1 no es mayor que 6. Vuelve a introducir un número: 8#
#Los números que has escrito son 6 y 8#


print("Introduce un número:")
num=int(input())
print("Introduce un número mayor que", num)
num2=int(input())
while num >= num2:
    if num2==num:
        print("Has introducido el mismo número.")
        print("Por favor, vuelve a introducir un número:")
        num2=int(input())
    elif num2<=num:
        print("Has introducido un número menor que el primero.")
        print("Por favor, vuelve a introducir un número:")
        num2=int(input())
print("Los números que has escrito son:", num, "y", num2)
