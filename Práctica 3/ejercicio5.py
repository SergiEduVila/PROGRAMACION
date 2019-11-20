#Sergi Vila Sánchez# #Práctica 3 Ejercicio 5#

#Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos 1, 99 i 213 pero no 1001). Si el usuario introduce un número de más de tres cifras debe un informar con un mensaje de error como este “ ERROR: El número 1005 tiene más de tres cifras”.#

print ("Introduce un número de 3 cifras máximo.")

num = int(input())

if num <= 999 and num >=-999:

    print (num)

else:
    print ("Error, el número", num, "tiene más de tres cifras.")
