#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 3#

#Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.#


print("Introduce un número:")
num1 = int(input())

print("Introduce un número mayor que ", num1)
num2 = int(input())

total=0
for i in range(num1, (num2 + 1)):
    total=total+i
    if i < num2:
        print(i, " + ", end=" ")
    else:
        print(i, " = ", total)
print("La suma de ",num1, " hasta ", num2," es de : ", total)
