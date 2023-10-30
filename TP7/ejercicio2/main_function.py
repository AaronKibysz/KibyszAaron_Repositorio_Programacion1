
from selection_sort_function import selection_sort

string_list = []
while True:
    string  = input('Ingrese un String o no ingrese ningun valor para finalizar:\n')
    if string != '':
        string_list.append(string)
    else:
        break

print(string_list)
print(selection_sort(string_list))