#Sergi Vila Sánchez# #Práctica 3 Ejercicio 6#

#Pida al usuario el precio de un producto y el nombre del producto y muestre el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale 100 euros y con el 21 % de IVA se queda en 121 euros en total”.#

print ("Introduce el nombre del producto.")

n_prod = input()

print ("Introduce el precio del producto")

p_prod = float(input())

pIVA = (21 * p_prod) / 100

ptotal = pIVA + p_prod

print ("Tu", n_prod, "vale", p_prod, " euros y con el IVA se queda en", ptotal, "euros.")
