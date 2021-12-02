
metros = 0
yarda = 0
pulgadas = 0
pies = 0

medida_metro = float(input("Ingrese la la medida en metros"))

while metros < medida_metro:
    metros = metros + 1
    yarda = metros * 1.094
    pulgadas = metros * 39.37
    pies = metros * 3.281

    print("metros=%s\t\t yardas=%.2f\t\t pulgadas=%.2f\t\tpies=%.2f\n" %(metros, yarda, pulgadas, pies))