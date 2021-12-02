

nombre_empleado = (input("Ingrese el nombre del empleado\n"))
tipo_empleado = float(input("Ingrese el tipo de empleado\n"))
numero_horas = float(input("Ingrese el numero de horas trabajadas\n"))
cuota = float(input("Ingrese la cuota\n"))
sueldo = 0

if tipo_empleado == 1:
    if numero_horas > 40:
       cuota = numero_horas * 1.5 * cuota
       sueldo = cuota
    else:
        print("No alcanza las horas requeridas")
else:
    if tipo_empleado == 2:
        cuota = numero_horas * 2 * cuota
        sueldo = cuota

    else:
        if tipo_empleado == 3:
            cuota = numero_horas * 2.5 * cuota
            sueldo = cuota


        else:
            if tipo_empleado == 4:
                cuota = numero_horas * 3 * cuota
                sueldo = cuota

            else:
                print("El tipo de empleado es incorrecto")



print("El sueldo a pagar es de\n %s\n"
      % sueldo)