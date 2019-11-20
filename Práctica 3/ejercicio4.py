#Sergi Vila Sánchez# #Práctica 3 Ejercicio 4#

#Pide al usuario que introduzca 3 calificaciones, y calcule la media de estas.#

print ("Introduce el nombre de la materia a evaluar")

asig = input()

print ("Introduce las 3 calificaciones para la media.")

nota1 = int(input())

nota2 = int(input())

nota3 = int(input())

n_media = (nota1 + nota2 + nota3) / 3

print ("La nota media de", asig, "es", n_media)
