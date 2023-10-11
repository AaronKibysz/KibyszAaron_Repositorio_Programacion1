# EJERCICIO 2
computer_age = -1
while computer_age<0:
    computer_age = int(input('Que edad tiene la computador: '))
    if computer_age<0:
        print('Ingrese un numero Positivo')
if computer_age > 2:
    print('La computadora es vieja')
else:
    print('La computadora es nueva')