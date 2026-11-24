# Renta de bicicletas usando funciones


# calcula el costo: precio por hora por numero de horas
def calcular_costo(precio, horas):
    costo = precio * horas
    return costo


# si son 4 horas o mas hay 15% de descuento
def calcular_descuento(costo, horas):
    if horas >= 4:
        descuento = costo * 0.15
    else:
        descuento = 0
    return descuento


# total = costo menos descuento
def calcular_total(costo, descuento):
    total = costo - descuento
    return total


# ----- programa principal -----
print("RENTA DE BICICLETAS")
print("")

nombre = input("Ingrese el nombre del cliente: ")

print("")
print("Tipos de bicicleta:")
print("1. Bicicleta estandar   $30 por hora")
print("2. Bicicleta de montana $50 por hora")
print("3. Bicicleta electrica  $80 por hora")

tipo = int(input("Elija el tipo de bicicleta (1, 2 o 3): "))

# si elige un numero que no existe se vuelve a pedir
while tipo < 1 or tipo > 3:
    print("Opcion no valida")
    tipo = int(input("Elija el tipo de bicicleta (1, 2 o 3): "))

if tipo == 1:
    bicicleta = "Estandar"
    precio = 30
elif tipo == 2:
    bicicleta = "Montana"
    precio = 50
else:
    bicicleta = "Electrica"
    precio = 80

horas = int(input("Ingrese el numero de horas de renta: "))

costo = calcular_costo(precio, horas)
descuento = calcular_descuento(costo, horas)
total = calcular_total(costo, descuento)

print("")
print("RESUMEN DE LA RENTA")
print("Cliente:", nombre)
print("Bicicleta:", bicicleta)
print("Precio por hora: $", precio)
print("Horas:", horas)
print("Costo de la renta: $", costo)

if descuento > 0:
    print("Tiene descuento del 15%: $", descuento)
else:
    print("No tiene descuento")

print("Total a pagar: $", total)
