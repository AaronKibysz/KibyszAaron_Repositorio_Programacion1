# EJERCICIO 16 FUNCION PRINCIPAL

from digit_search import digit_search_in_number

number = int(input('Ingrese un numero entero:\n'))
while True:
    digit = input('Ingrese un digito:\n')
    if len(digit) != 1:
        print('Ingrese 1 digito')
    else:
        digit = int(digit)
        break

print(f'Se ha encontrado {digit_search_in_number(number, digit)} veces el digito {digit} en el numero {number}')