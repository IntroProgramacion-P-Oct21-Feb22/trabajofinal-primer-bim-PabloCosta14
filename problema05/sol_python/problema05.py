

valorx = float(input("Ingrese el valor de X"))
valory = float(input("Ingrese el valor de Y"))

coordenadas = ("(%s,%s)" %(valorx,valory))
if valorx > 0 and valory > 0:
    cuadrante = "cuadrante I"
else:
    if valorx < 0 and valory > 0:
        cuadrante = "cuadrante II"
    else:
        if valorx < 0 and valory < 0:
         cuadrante = "cuadrante III"
        else:
            if valorx > 0 and valory < 0:
                cuadrante = "cuadrante IV"


print("Las coordenadas ingresadas son:%s\nEstan ubicadas en el cuadrante: %s\n"%(coordenadas, cuadrante))


