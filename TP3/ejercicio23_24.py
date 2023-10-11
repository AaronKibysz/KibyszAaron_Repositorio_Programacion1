# EJERCICIO 23 y 24
amount_list = []
addition = 0
while True:
    amount = float(input('Ingrese el monto de la compra o "0" para finalizar: '))
    if amount<0:
        print('Ingrese un monto valido')
    elif amount>0:
        addition += amount
        amount_list.append(amount)
    else:
        break;

if addition>1000:
    print(f'El monto a pagar con un %10 de descuento es ${addition*0.9}')
else:
    print(f'El monto a pagar es ${addition}')