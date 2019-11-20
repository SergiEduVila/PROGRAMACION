#Sergi Eduard Vila Sánchez# #Práctica 7 Ejercicio 1#

#Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.#


print("Escribe un texto cualquiera:")
texto=input()
def proc(a):
    print("")
    print("Versión en minúsculas:")
    print(a.lower())
    print("")
    print("Versión en mayúsculas:")
    print(a.upper())
proc(texto)
