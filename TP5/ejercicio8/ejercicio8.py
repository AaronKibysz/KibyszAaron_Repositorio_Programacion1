#EJERCICIO 8 FUNCION PRINCIPAL

from circle import circle_calculator

while True:
    radius = float(input('Ingrese el radio del circulo:\n'))
    if radius > 0:
        break
    print('Ingrese un numero valido para el radio(numero mayor a 0)')

perimeter, area = circle_calculator(radius)

print(f'Con el radio de {radius} se sabe que:\nEl PERIMETRO del circulo es: {perimeter}\nEl AREA del circulo es: {area}')