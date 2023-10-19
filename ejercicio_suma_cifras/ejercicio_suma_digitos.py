### EJERCICIO SUMA DIGITOS CLASE 19/10/2023 ###

from suma_cifras import number_addition

print('Bienvenido a la suma de digitos\n')

number_sum = 0
while True:
    number = int(input('Ingrese un numero entero o ingrese "0" para finalizar: '))
    if number != 0:
        number_sum += number
        print(f'La suma de los digitos de {number} es: {number_addition(number)}')
    else:
        break

print(f'La suma de todos los numeros ingresados es: {number_sum}')
print(f'Y la suma de los digitos es {number_addition(number_sum)}')