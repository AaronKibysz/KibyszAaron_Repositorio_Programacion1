#EJERCICIO 7 FUNCION PRINCIPAL

from min_max_calculator import min_max_funtion

number_list = []
while True:
    try:
        number = input('Ingrese un valor numerico para sumar a la lista o no ingrese nada para terminar de sumar numeros a la lista:\n')
        if number == '':
            break
        number_list.append(float(number))
    except ValueError:
        print('Valor invalido, PRUEBE NUEVAMENTE')

min_num, max_num = min_max_funtion(number_list)
print(f'El numero menor de la lista es {min_num}\nY el numero mayor de la lista es {max_num}')