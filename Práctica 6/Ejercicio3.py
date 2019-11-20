#Sergi Eduard Vila Sánchez# #Práctica 6 Ejercicio 3#

#Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.#
#Escribe una nota: 7.5#
#Escribe una nota: 0#
#Escribe una nota: 10#
#Escribe una nota: -1#
#Las notas que has Escrito son [7.5, 0.0, 10.0]#


print("Introduce las notas de los exámenes:")
nota=float(input())
lnota=[]
if nota >=0 and nota <=10:
    lnota.append(nota)
while nota >=0 and nota <=10:
    print("Introduce las notas de los exámenes:")
    nota=float(input())
    if nota >=0 and nota <=10:
        lnota.append(nota)
print("Las notas que has introducido son:", lnota)
