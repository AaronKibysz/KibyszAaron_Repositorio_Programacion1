
from character_count_function import character_count

string_list = []
for i in range(50):
    string = input(f'Ingrese el String Numero {i} para agreagr a la lista:\n')
    if string == '':
        print('Por favor no ingrese un String vacio, Ingrese de nuevo!!')
    else:
        string_list.append(string)

character_dicc = character_count(string_list)
for key, value in character_dicc.items():
    print(f'"{key}": {value}')