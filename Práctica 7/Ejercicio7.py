#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 7#

#Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.#


print("Escribe una frase cualquiera:")
frase=input()
def f(frase):
    A=frase.count("A")
    a=frase.count("a")
    E=frase.count("E")
    e=frase.count("e")
    I=frase.count("I")
    i=frase.count("i")
    O=frase.count("O")
    o=frase.count("o")
    U=frase.count("U")
    u=frase.count("u")
    a=a+A
    e=e+E
    i=i+I
    o=o+O
    u=u+U
    print("Hay", a,"letras 'a'.")
    print("Hay", e,"letras 'e'.")
    print("Hay", i,"letras 'i'.")
    print("Hay", o,"letras 'o'.")
    print("Hay", u,"letras 'u'.")
f(frase)
