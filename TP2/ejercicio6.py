# EJERCICIO 6

year = int(input('Ingrese el anio: '))
if (year%4 == 0 and (not year%100 == 0) or year%400 == 0):
    print('El anio es biciesto')