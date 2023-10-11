# EJERCICIO 13
print('Ingrese SALIR para Salir: ')
while True:
    string = input()
    string_upper = string.upper()
    if string_upper != 'SALIR':
        print(string)
    else:
        break;