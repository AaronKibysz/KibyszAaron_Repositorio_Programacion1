
from insertion_sort_function import insertion_sort

string_list = []

while True:
    string = input('Ingrese un String para agregar a la lista o no ingrese nada para finalizar:\n')
    if string == '':
        break
    else:
        string_list.append(string)

for string in insertion_sort(string_list):
    print(string)