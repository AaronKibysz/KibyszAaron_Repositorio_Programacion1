# EJERCICIO 19

while True: 
    pencil = int(input('Cuantos lapices se van a comprar: '))
    if pencil>0:
        break;
    else:
        print('Ingrese un valor valido!!')

if pencil < 1000:
    print('La cantidad a pagar es: $', pencil*60)
else:
    print('La cantidad a pagar con un descuento del %7 es: $', (pencil*60)*0.93)