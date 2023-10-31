
from count_digits_function import count_digits

while True:
    number = int(input('Ingrese un numero entero positivo:\n'))
    if number > 0:
        break
    else:
        print('Ingrese un valor valido\n')

print(count_digits(number))