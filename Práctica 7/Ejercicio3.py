#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 3#

#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste debe mostrar la frase con un carácter en cada línea.#


print("Escribe una frase cualquiera:")
texto=input()
def proc(a):
    for i in range(len(a)):
        print(a[i])
proc(texto)
