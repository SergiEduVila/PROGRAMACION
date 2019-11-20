#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 6#

#Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo imprimirá el programa principal por pantalla.#


print("Introduce tu nombre:")
nombre=input()
print("Introduce un carácter:")
letra=input()
def f(nombre,letra):
    nombre=nombre.lower()
    letra=letra.lower()
    existe=True
    buscar=int()
    buscar=nombre.count(letra)
    if buscar == 0:
        existe=False
    return existe
existe=(f(nombre,letra))
if existe==True:
    print("La letra", letra, "figura en el nombre", nombre)
else:
    print("La letra", letra, "no figura en el nombre", nombre)
