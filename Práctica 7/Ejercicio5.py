#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 5#

#Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada. Devolverá la función la frase modificada, y el programa principal la imprimirá.#


print("Introduce un texto:")
texto=input()
print("Introduce una vocal ahora:")
vocal=input()
def f(a,b):
    a=a.replace("A",b)
    a=a.replace("a",b)
    a=a.replace("E",b)
    a=a.replace("e",b)
    a=a.replace("I",b)
    a=a.replace("i",b)
    a=a.replace("O",b)
    a=a.replace("o",b)
    a=a.replace("U",b)
    a=a.replace("u",b)
    return a
print("La frase ahora es:", end=" ")
print(f(texto,vocal))
print(" ")
