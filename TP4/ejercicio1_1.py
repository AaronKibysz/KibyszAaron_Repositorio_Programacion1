# EJERCICIO 1_1

line_list = []
while True:
    line = input('Ingrese una linea o deje en blanco para finalizar: ')
    if not line:
        break;
    line_list.append(line)

for line in line_list:
    print(line.upper())