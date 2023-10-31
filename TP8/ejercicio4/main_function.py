
from parity_function import *

while True:
    number = int(input('ingrese un numero entero positivo:\n'))
    if number > 0:
        break
    else:
        print('Ingrese un numero valido')

print(f'el numero {number} es par?: {even(number)}')