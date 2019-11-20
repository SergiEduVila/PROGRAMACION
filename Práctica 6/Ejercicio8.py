#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 8#

#Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números.#
#Escribe límite: 50#
#Escribe un valor: 10#
#Escribe otro valor: 45#
#45 es demasiado grande. Escribe otro valor: 1#
#Escribe otro valor: 39#
#El límite a alcanzar es 50. La lista creada es: 10, 1, 39#


print("Introduce un número límite:")
num=int(input())
limite=num
resto=num
nlista=[]
sumatotal=0
print("Introduce otro número cualquiera:")
num=int(input())
while num > resto:
    print(num, "es demasiado grande. Escribe otro valor:")
    num=int(input())
nlista.append(num)
resto=resto-num
sumatotal=sumatotal+num
while sumatotal!=limite:
    print("Introduce otro número cualquiera:")
    num=int(input())
    if num > resto:
        print(num, "es demasiado grande. Escribe otro valor:")
        num=int(input())
    resto=resto-num
    nlista.append(num)
    sumatotal=sumatotal+num
print("El número límite a alcanzar es:", limite, end=" ")
print("La lista creada es:", nlista[0], end=" ")
for i in range(1, len(nlista)):
    print(",", nlista[i], end="")
print(".")
