#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 7#

#Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.#
#Escribe límite: 50#
#Escribe un valor: 10#
#Escribe otro valor: 25#
#Escribe otro valor: 7#
#Escribe otro valor: 14#
#El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56#


print("Introduce un número límite a sobrepasar:")
limite=int(input())
print("Ahora introduce los números que quieras:")
num=int(input())
nlista=[]
sumatotal=num
while sumatotal<=limite:
    nlista.append(num)
    print("Introduce otro número cualquiera:")
    num=int(input())
    sumatotal=sumatotal + num
nlista.append(num)
print("El límite ha superar es:", limite, end=" ")
print("La lista de números creada es:", nlista[0], end=" ")
for i in range(1, len(nlista)):
    print(",", nlista[i], end="")
print(", ya que la suma de estos números es de:", sumatotal)
print(".")
print("")
