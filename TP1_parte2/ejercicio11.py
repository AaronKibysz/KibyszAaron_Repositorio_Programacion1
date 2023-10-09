# EJERCICIO 11

number1 = int(input('Ingrese el numero 1: '))
number2 = int(input('Ingrese el numero 2: '))
distance = 0
if number1 > number2:
    distance = number1 - number2
else:
    distance = number2 - number1

if distance == 0:
    print('No hay distancia entre los numeros ingresados ya que ambos son iguales')
else:
    print('La distancia entre ambos numeros es de: |',distance,'|')