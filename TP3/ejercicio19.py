# EJERCICIO 19

while True:
    number_max = float(input("Ingrese el monto objetivo: "))
    if number_max<0:
        print('Ingrese un monto valido')
    else:
        break;

number_addition = 0
while number_addition<number_max:
    while True:
        number = float(input('Cuanto va a sumar?: '))
        if number<0:
            print('Ingrese un monto valido')
        else:
            number_addition += number
            break;