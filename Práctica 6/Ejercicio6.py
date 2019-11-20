#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 6#

#Escribe un programa que pida primero dos números (máximo y mínimo) y que después te pida números intermedios. Para terminar de escribir números, escribe un número que no esté comprendido entre los dos valores iniciales. El programa termina escribiendo la lista de números.#
#Escribe un número: 6#
#Escribe un número mayor que 6: 4#
#4 no es mayor que 6. Vuelve a probar: 50#
#Escribe un número entre 6 y 50: 45#3
#Escribe otro número entre 6 y 50: 13#
#Escribe otro número entre 6 y 50: 4#
#Los números situados entre 6 y 50 que has escrito son: 45, 13#



#<<<<MANERA CON DOBLE LISTA>>>>#

#print("Introduce un número:")
#minimo=int(input())
#print("Escribe un número mayor que", minimo)
#maximo=int(input())
#while maximo<=minimo:
#    if maximo<minimo:
#        print(maximo, "és menor que ", minimo, ".Vuelve a introducir otro número:")
#        maximo=int(input())
#    elif maximo==minimo:
#        print(maximo, "és igual que ", minimo, ".Vuelve a introducir otro número:")
#        maximo=int(input())
#print("Introduce ahora un número entre ", minimo, "y", maximo)
#num=int(input())
#nlist=[]
#listofnlist=[]
#while num>minimo and num<maximo:
#    nlist.append(num)
#    listofnlist.append(nlist[0])
#    del nlist[0]
#    print("Introduce otro número que esté entre", minimo, "y", maximo)
#    num=int(input())
#print("Los números situados entre ", minimo, "y", maximo, "que has escrito son:", end=" ")
#print(listofnlist[0], end="")
#for i in range(1, len(listofnlist)):
#    print(",", listofnlist[i], end="")
#print(".")
#print("")#



#<<<<MANERA CON 1 LISTA>>>>#

print("Introduce un número:")
minimo=int(input())
print("Escribe un número mayor que", minimo)
maximo=int(input())
while maximo<=minimo:
    if maximo<minimo:
        print(maximo, "és menor que ", minimo, ".Vuelve a introducir otro número:")
        maximo=int(input())
    elif maximo==minimo:
        print(maximo, "és igual que ", minimo, ".Vuelve a introducir otro número:")
        maximo=int(input())
print("Introduce ahora un número entre ", minimo, "y", maximo)
num=int(input())
nlist=[]
while num>minimo and num<maximo:
    nlist.append(num)
    print("Introduce otro número que esté entre", minimo, "y", maximo)
    num=int(input())
print("Los números situados entre ", minimo, "y", maximo, "que has escrito son:", end=" ")
print(nlist[0], end="")
for i in range(1, len(nlist)):
    print(",", nlist[i], end="")
print(".")
print("")
