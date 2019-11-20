#Sergi Vila Sánchez Eduard# #Práctica 5 Ejercicio 4#

#Escribe un programa que pida un número y calcule su factorial.#

print("Introduce un número:")
num1=int(input())
factorial=1
for i in  range(1, (num1+1)):
    factorial=factorial*i
print("El factorial de ", num1, " es de: ", factorial)
