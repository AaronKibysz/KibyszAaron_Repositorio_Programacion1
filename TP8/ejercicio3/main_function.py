
from sub_string_position_function import sub_string_position

while True:
    string = input('Ingrese un string:\n')
    if string != '':
        break
    else:
        print('Ingrese un string no vacio')
while True:
    string2 = input('Ingrese un segundo sting:\n')
    if string2 != '':
        break
    else:
        print('Ingreese un string no vacio')

print(sub_string_position(string, string2))