#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 2#

#Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares.#


print("Introduce un número.")
num1 = int(input())

print("Introduce un número mayor que ", num1)
num2 = int(input())

for i in range(num1, (num2+1)):
    residuo=i%2
    if residuo != 0:
        print(i, " es impar. ")
    else:
        print(i, " es par.")
