# EJERCICIO 5 FUNCION PRINCIPAL
from temp_med import temp_med_funtion

print('Calculadora de Temperatura Media')

while True:
    days_count = int(input('Ingrese cuantos dias quiere ingresar:\n'))
    if days_count < 1:
        print('Al menos ingrese 1 dia')
    else:
        break

i = 0
temp_dict = {}
while i < days_count:
    print(f'DIA {i+1}')
    max_temp = float(input('Ingrese la temperatura maxima:\n'))
    min_temp = float(input('Ingrese la temperatura minima:\n'))
    if max_temp < min_temp:
        print('La temperatura maxima ingresada es menor a la minima, Ingrese las temperaturas nuevamente')
        continue
    med_temp = temp_med_funtion(max_temp, min_temp)
    temp_dict.update({i+1 : med_temp})
    i += 1

for days, temp in temp_dict.items():
    print(f'La temperatura media del dia {days} es: {temp}')