# EJERCICIO 6
import random

number_list = []
for i in range(random.randrange(1, 100)):
    number_list.append(random.randint(1, 100))

for i in range(random.randrange(1,100)):
    number = int(input('Ingrese un numero entero positivo para buscar en al lista: '))
    if number in number_list:
        break;

if(number in number_list):
    print(f'Se ha encontrado el numero {number} en la lista')
else:
    print('No se ha encontrado ninguna coincidencia en la lista')