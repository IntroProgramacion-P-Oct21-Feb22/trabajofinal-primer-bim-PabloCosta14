

val1 = 2
contador = 2
val2 = 0
cadena = 0
numero = (int(input("Ingrese el numero par")))

if  numero > 2 and numero % 2 == 0:
    print("La suma de los numeros pares hasta el numero ingresado es")

    while contador <= numero:
        contador = contador + 2

        val2 = val2 + 1
        total = val1 * val2
        cadena = total + cadena

    print(cadena)
else:
    print ("Numero Ingresado erróneo")


