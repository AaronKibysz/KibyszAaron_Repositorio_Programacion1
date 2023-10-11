# EJERCICIO 21

number_list = []

while True:
    number = int(input('Ingrese numeros enteros positivos o "0" para finalizar: '))
    if number < 0:
        print('Ingrese un numero valido')
    elif number > 0:
        number_list.append(number)
    else:
        break;

number_max = max(number_list)
print(f'El numero maximo ingresado es {number_max}')