cantidad_trajes = int(input("Ingrese la cantidad de trajes"))
costo_trajes = float(input("Ingrese el precio de los trajes"))

subtotal = costo_trajes * cantidad_trajes

if cantidad_trajes == 1:
    descuento = 20 * subtotal / 100
    valortotal = subtotal - descuento
    descuento_realizado = 20
else:
    if cantidad_trajes == 2:
        descuento = 25 * subtotal / 100
        valortotal = subtotal - descuento
        descuento_realizado = 25
    else:
        if cantidad_trajes == 3:
            descuento = 40 * subtotal / 100
            valortotal = subtotal - descuento
            descuento_realizado = 40
        else:
            descuento = 50 * subtotal / 100
            valortotal = subtotal - descuento
            descuento_realizado = 50

print("El subtotal al pagar es %s\nEl descuento es %s\nEL total a pagar es %s\n"
      %(subtotal, descuento_realizado, valortotal))