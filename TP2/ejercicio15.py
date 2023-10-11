# EJERCICIO 15
import math
while True:
    option = input('Quiere Calcular el Area de un TRIANGULO o la de un CIRCULO (T o C): ')
    option = option.upper()
    if option != 'T' and option != 'C':
        print('Ingrese una opcion Valida!!')
    else:
        break;

if option == 'C':
    radius = float(input('ingrese el RADIO del Circulo: '))
    pi = math.pi
    area = pi*(radius**2)
    print('El area del Circulo es: ', area)
else:
    base = float(input('Ingrese la Base del Triangulo: '))
    height = float(input('Ingrese la Altura del triangulo: '))
    area = (base*height)/2
    print('El area del triangulo es: ', area)