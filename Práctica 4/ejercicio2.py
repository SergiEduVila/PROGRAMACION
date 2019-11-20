#Sergi Vila Sánchez Eduard# #Práctica 4 Ejercicio 2#

#Pida al usuario 5 números y diga si estos estaban en orden decreciente, creciente o desordenados.#

print ("Introduce cinco números.")

n1 = int(input())

n2 = int(input())

n3 = int(input())

n4 = int(input())

n5 = int(input())


if n1 == n2 and n2 == n3 and n3 == n4 and n4 == n5:

    print("Los números introducidos son iguales.")

elif n1 >= n2 and n2 >= n3 and n3 >= n4 and n4 >= n5:

    print("Los números introducidos están en orden decreciente.")

elif n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:

    print("Los números introducidos están en orden creciente.")

else:

    print("Los números introducidos están desordenados.")
