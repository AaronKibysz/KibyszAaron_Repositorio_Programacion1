
from number_itterator import number_less_generator
from number_count_function import number_count

number_list = []

while True:
    number = float(input('Ingrese un numero para aniadir a la lista o ingrese 0 para finalzar:\n'))
    if number == 0:
        break
    else:
        number_list.append(number)

number_check = float(input('Ingrese un numero que quiera eliminar de la lista!!\n'))
if number_check in number_list:
    number_list.remove(number_check)
    print(f'Se ha eliminado el numero {number_check} de la Lista')
else:
    print(f'No se ha encontrado ocurrencia del numero {number_check} en la lista')

print(f'La sumatoria de todos los numeros ingresados en la lista es: {sum(number_list)}')

number_gen = float(input('Ingrese un numero para crear una nueva lista:\n'))

number_list2 = number_less_generator(number_list, number_gen)
print(f'La segunda lista quedaria como f{number_list2}')

number_count_list = number_count(number_list)
print(f'La tercera lista quedaria f{number_count_list}')