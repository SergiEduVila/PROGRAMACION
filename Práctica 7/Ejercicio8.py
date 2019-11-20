#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 8#

#Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final.#


print("Escribe uan frase cualquiera:")
frase=input()
def f(frase):
    frase=frase.replace(" ", "")
    return frase
print("La frase ahora es:")
print(f(frase))
