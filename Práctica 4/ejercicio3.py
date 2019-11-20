#Sergi Vila Sánchez Eduard# #Práctica 4 Ejercicio 3#

#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.#


print("Escoge que quieres calcular, para ello, escribe el número que hay delante de cada opción:")
print("1. Triangulo.")
print("2. Quadrado.")

elec = int(input())

if elec == 1:

    print("Bienvenido a Triangulo Zone.") 
    print("Introduce el tipo de unidad métrica que deseas utilizar (mm, cm, dm, m, dam, hm, km):")

    umt = input()

    print("Introduce los datos requeridos para calcular el suculento triangulo deseado.")
    print("ALTURA (h):")

    h = int(input())

    print("BASE (b):")

    b = int(input())

    at = (b * a) / 2

    print("El área del triangulo es de", at, umt, "quadrados.")
    
elif elec == 2:

    print("Bienvenido a Quadrado Zone.")
    print("Introduce el tipo de unidad métrica que deseas utilizar (mm, cm, dm, m, dam, hm, km):")

    umq = input()

    print("Introduce los datos requeridos para calcular el suculento quadrado deseado.")
    print("CATETO:")

    c = int(input())

    aq = c**2

    print("El área del quadrado es de", aq, umq, "quadrados.")

else:

    print("ERROR LOL, aprende a escribir faggot, que no es tan difícil escribir 1 o 2.")
