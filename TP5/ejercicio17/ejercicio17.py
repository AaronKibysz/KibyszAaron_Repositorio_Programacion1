# EJERCICIO 17 FUNCION PRINCIPAL

from digit_add import digit_addition
from factorial import factorial_calculator

number_list = []
while True:
    number = int(input('Ingrese numeros primos para agragar a la lista, o no para finalizar:\n'))
    prime_verificator = True
    for i in range(2, number-1):
        if number%i == 0:
            prime_verificator = False
            break
    if prime_verificator == False:
        break
    number_list.append(number)

try:
    while True:
        digit_coin = input('Ingrese un digito para buscar coincidencias:\n')
        if len(digit_coin) == 1:
            digit_coin = int(digit_coin)
            break
        else:
            print('Ingrese una opcion valida')
except ValueError:
    print('valor invalido, pruebe de nuevo')

digit_addition(number_list, digit_coin)
print(f'Y el numero factorial del mayor valor ingresado {max(number_list)} es {factorial_calculator(number_list)}')