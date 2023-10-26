# EJERCICIO 15 FUNCION PRINCIPAL

from factorial import factorial_calculator

number_list = []

try:
    while True:
        number = input('Ingrese un numero entero o no ingrese nada para terminar de aniadir numeros:\n')
        if number == '':
            break
        number = int(number)
        if number < 0:
            print('Debe ingresar un numero mayor o igual a 1')
            continue
        number_list.append(number)
except ValueError:
    print('Ingrese un valor Valido')

print(f'La cantidad de numeros a los cuales se les calculo el factorial es: {factorial_calculator(number_list)}')