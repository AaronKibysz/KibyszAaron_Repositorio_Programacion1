# EJERCICIO 14 FUNCION PRINCIPAL

from prime_number_function import prime_number_calculator

while True:
    number = int(input('Ingrese un numero entero positivo:\n'))
    if number < 1:
        print('Ingrese un valor mayor o igual a 1')
    else:
        break

prime_verificator = False
prime_verificator = prime_number_calculator(number)

if prime_verificator == True:
    print(f'El numero {number} No es Primo')
else:
    print(f'El numero {number} Es Primo')