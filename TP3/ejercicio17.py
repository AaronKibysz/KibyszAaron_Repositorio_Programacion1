# EJERCICIO 17

vocals_list = []
vocals = ('A', 'E', 'I', 'O', 'U')
string = input('Ingrese una frase: ')
string = string.upper()

for i in string:
    if i in vocals:
        if not i in vocals_list:
            vocals_list.append(i)

print(f'Las vocales que aparecen en la frase son: ', vocals_list)