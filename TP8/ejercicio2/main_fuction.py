
from multiple_of_fuction import multiple_of

while True:
    n = int(input('Ingrese el primer numero entero positivo:\n'))
    if n > 0:
        break
    else:
        print('Ingrese un numero valido')

while True:
    b = int(input('Ingrese el segundo numero entero positivo:\n'))
    if b > 0:
        break
    else:
        print('Ingrese un numero valido')

print(multiple_of(n, b))