
from bubble_sort_funtion import bubble_sort

number_list = []
while True:
    number = int(input('Ingrese un valor entero o ingrese "0" para finalizar de ingresar numeros:\n'))
    if number != 0:
        number_list.append(number)
    else:
        break

print(number_list)
print(bubble_sort(number_list))