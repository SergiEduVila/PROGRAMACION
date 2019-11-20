#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 2#

#Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.#


print("Introduce tu primer nombre:")
nombre=input()
print("Introduce ahora tu primer apellido:")
ape1=input()
print("Introduce por último tu segundo apellido:")
ape2=input()
def proc(a,b,c):
    nombre=a+" "+b+" "+c
    print(nombre)
proc(nombre,ape1,ape2)
