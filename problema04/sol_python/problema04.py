

numero1 = float(input("ingrese el valor del primer numero"))
numero2 = float(input("ingrese el valor del segundo numero"))
numero3 = float(input("ingrese el valor del tercer numero"))
respuesta = 0

if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Los numeros ingresados no son validos")
else:
    if numero1 > numero2 and numero1 > numero3:
        respuesta = numero1

    else:
        if numero2 > numero1 and numero2 > numero3 :
            respuesta = numero2

        else:
            if numero3 > numero1 and numero3 > numero2:
                respuesta = numero3

print("la respuesta es\n%s\n"% (respuesta))
