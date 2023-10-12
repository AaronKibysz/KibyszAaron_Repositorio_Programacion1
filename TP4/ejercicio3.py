# EJERCICIO 3

number_list = []
while True:
    number = int(input('Ingrese un numero entero positivo mayor a 1 o "0" para finalizar: '))
    if number>1:
        number_list.append(number)
    elif number<0 or number == 1:
        print('No se puede ingresar numeros negativos o iguales a 1!!!')
    elif number == 0:
        break

amount_prime_number = 0
for number in number_list:
    prime_verificator = True
    for i in range(number-1,2,-1):
        if number%i == 0:
            prime_verificator = False
            break
    if prime_verificator == True:
            amount_prime_number += 1

print(f'El numero de valor primos ingresado es {amount_prime_number}')