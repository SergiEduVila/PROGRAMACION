#Sergi Eduard Vila Sánchez# #Práctica 5 Ejercicio 12#

#Escribe un programa que pida un número y escriba si primo o no.#
#Dame un número: 123#
#El número 123 no es primo#
#Dame un número:127#
#El número 127 es primo#

#VERSION 1 (MÍA)#
print("Introduce un número cualquiera:")
num=int(input())
primo=False
no_primo=False
for i in range(2, num):
    resto=num%i
    if resto!=0:
        primo=True
    elif resto ==0:
        no_primo=True

if no_primo==False:
    print("El número", num, "és primo.")
elif no_primo==True:
    print("El número", num, "no és primo.")




#VERSION 2 (RAFA)#
print("Introduce un número cualquiera:")
num=int(input())
primo=True

for i in range(2, num):    
    if num%i==0:
        primo=False
    
if primo:
    print("El número", num, "és primo.")
else:
    print("El número", num, "no és primo.")
