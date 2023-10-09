# EJERCICIO 8

base = float(input('Ingrese sueldo base: '))

sold_list = []
for i in range(0, 3):
    sold_list.append(float(input('Ingrese valor de venta: ')))

commision = 0
for number in sold_list:
    commision += (number*0.1)

sueldo = commision+base
print('A final de mes cobrara el valor de: $', sueldo)