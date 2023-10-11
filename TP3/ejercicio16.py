# EJERCICIO 16

while True:
    amount = int(input('Cuantos numeros quiere ingresar: '))
    if amount<1:
        print('Ingrese un valor valido')
    else:
        break;

negative_count = 0
for i in range(amount):
    number = int(input('Ingrese un numero: '))
    if number < 0:
        negative_count += 1

print(f'Se han ingresado {negative_count} numeros negativos')