#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 5#

#Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. El programa termina escribiendo la lista de números:#
#Escribe un número: 6#
#Escribe un número mayor que 6: 10#
#Escribe un número mayor que 10: 12#
#Escribe un número mayor que 12: 25#
#Escribe un número mayor que 25: 9#
#Los números que has escrito son: 6, 10, 12, 25  (Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista, haced esto así a partir de ahora)#


print("Introduce un número:")
num=int(input())
nlist=[]
listlist=[]
nlist.append(num)
listlist.append(nlist[0])
print("Introduce un número mayor que:", nlist[0])
num=int(input())
while num>nlist[0]:
    del nlist[0]
    nlist.append(num)
    listlist.append(nlist[0])
    print("Introduce un número mayor que:", nlist[0])
    num=int(input())

print("Los números escritos son:", end=" ")
print(listlist[0], end="")
for i in range(1, len(listlist)):
    print(",", listlist[i], end="")
print(".")
print("")
