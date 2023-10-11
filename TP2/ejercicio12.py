# EJERCICIO 12

current_age = int(input('Ingrese el anio actual: '))
random_age = int(input('Ingrese un anio aleatorio: '))

if current_age>random_age:
    print('Han pasado', current_age-random_age, 'anios desde', random_age, 'hasta la actualidad')
else:
    print('Faltan', random_age-current_age, 'anios para', random_age)