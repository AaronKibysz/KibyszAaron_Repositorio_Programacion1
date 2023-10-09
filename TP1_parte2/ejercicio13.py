# EJERCICIO 13

number = 0
while number<10 or number>99:
    number = int(input('Ingrese un numero de 2 cifras: '))

number2 = ''
for digit in reversed(str(number)):
    number2 = number2 + digit

print(number2)