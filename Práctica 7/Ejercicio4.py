#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 4#

#Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. La función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el resultado para que el programa principal la imprima por pantalla.#


print("Escribe una frase cualquiera:")
texto=input()
def f(a):
    b=a.replace(" ","*")
    return b
print (f(texto))
