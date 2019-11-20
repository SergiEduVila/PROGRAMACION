#Sergi Vila Sánchez Eduard# #Práctica 4 Ejercicio 4#

#Pida al usuario tres números y un cuarto número, y compruebe si éste último es divisor de los tres números primeros.#


print("Introduce tres números qualesquiera.")

n1 = int(input())

n2 = int(input())

n3 = int(input())

print("Introduce ahora un cuarto número.")

cuatro = int(input())

d1 = n1 % cuatro

d2 = n2 % cuatro

d3 = n3 % cuatro


if d1 == 0 and d2 == 0 and d3 == 0:

    print("El cuarto número es divisor de los tres números.")

elif d1 == 0 and d2 == 0:

    print("El cuarto número solo es divisor del primer y segundo número.")

elif d2 == 0 and d3 == 0:

    print("El cuarto número solo es divisor del segundo y tercer número.")

elif d1 == 0 and d3 == 0:

    print("El cuarto número solo es divisor del primer y tercer número.")

elif d1 == 0:

    print("El cuarto número solo es divisor del primer número.")

elif d2 == 0:

    print("El cuarto número solo es divisor del segundo número.")

elif d3 == 0:

    print("El cuarto número solo es divisor del tercer número.")

else:

    print("El cuarto número no es divisor de ninguno de los números.")
