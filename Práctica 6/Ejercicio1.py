#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 1#

#Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.#
#Escribe una palabra: viaje#
#Escribe más palabras: aventura#
#Escribe más palabras: cómic#
#Escribe más palabras:#
#Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']#


print("Escribe palabras:")
palabra=input()
lista_palabra=[]
if palabra != "":
    lista_palabra.append(palabra)
while palabra != "":
    print("Escribe otras palabras:")
    palabra=input()
    if palabra != "":
        lista_palabra.append(palabra)
print("La lista de palabras que has escrito es: ", lista_palabra)
