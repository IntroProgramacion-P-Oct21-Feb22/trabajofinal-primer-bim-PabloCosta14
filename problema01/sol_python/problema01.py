

anguloA = float(input("Ingrese el valor del angulo A\n"))
anguloB = float(input("Ingrese el valor del angulo B\n"))
anguloC = float(input("Ingrese el valor del angulo C\n"))

if anguloA == 90 or anguloB == 90 or anguloC == 90:
    tipo_triangulo = "Rectangulo"
else:
    if anguloA > 90 and anguloA <= 180 or anguloB > 90 and anguloB <= 180 or anguloC > 90 and anguloC <= 180:
        tipo_triangulo = "Obtusangulo"
    else:
        if anguloA < 90 or anguloB < 90  or  anguloC < 90:
            tipo_triangulo = "Acutangulo"

print("el triangulo es de tipo\n",tipo_triangulo )