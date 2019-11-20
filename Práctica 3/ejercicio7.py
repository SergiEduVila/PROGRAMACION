#Sergi Vila Sánchez# #Práctica 3 Ejercicio 7#

#Pida al usuario tres número que serán el día, mes y año. Comprueba que la fecha introducida es válida.#

print("Introduce el día.")

dia = int(input())

if dia > 31:

    print("Día incorrecto.")

print("Introduce el mes.")

mes = int(input())

if mes > 12:

    print("Mes incorrecto.")

print("Introduce el año.")

year = int(input())


if mes==2:

    if dia <= 28:

        if dia < 10:

            print("0",dia,"/",mes,"/",year)

        elif mes < 10:

            print(dia,"/0",mes,"/",year)

        elif dia <10 and mes < 10:

            print("0",dia,"/0",mes,"/",year)

        else:

            print(dia,"/",mes,"/",year)

    else:

        print("Fecha incorrecta.")

elif mes != 2:

    if dia <= 30:

        if dia < 10:

            print("0",dia,"/",mes,"/",year)

        elif mes < 10:

            print(dia,"/0",mes,"/",year)

        elif dia <10 and mes < 10:

            print("0",dia,"/0",mes,"/",year)

        else:

            print(dia,"/",mes,"/",year)


    elif dia == 31:

        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

            if dia < 10:

                print("0",dia,"/",mes,"/",year)

            elif mes < 10:

                print(dia,"/0",mes,"/",year)

            elif dia <10 and mes < 10:

                print("0",dia,"/0",mes,"/",year)

            else:

                print(dia,"/",mes,"/",year)

        else:

            print("Fecha incorrecta.")
