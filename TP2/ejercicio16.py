# EJERCICIO 16

option_tuple = ('1', '2', '3', '4')
print('CALCULADORA DE FUNCIONES BASICAS')
a = float(input('Ingrese el valor de A: '))
b = float(input('Ingrese el valor de B: '))

print('INGRESE LA OPCION QUE QUIERE REALIZAR')
while True:
    option = input('1 - SUMA\n2 - MULTIPLICACION\n3 - RESTA\n4 - DIVISION\n')
    if not option in option_tuple:
        print('Ingrese una opcion valida!!')
    else:
        break;

if option == '1':
    print('La suma es: ', a+b)
elif option == '2':
    print('La multiplicacion es: ', a*b)
elif option == '3':
    print('La resta es: ', a-b)
else:
    if b != 0:
        print('La division es: ', a/b)
    else:
        print('No se puede dividir ya que el divisor es 0')