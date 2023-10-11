# EJERCICIO 13

number1 = int(input("Ingrese un numero entero: "))
if number1 == 0:
    print('El numero ingresado es nulo')
elif number1 < 0:
    print('El numero ingresado es negativo')
number2 = int(input("Ingrese el segundo numero: "))
if number2 < 0:
    print('El numero ingresado es negativo')
elif number2 == 0:
    print('El numero ingresado es nulo')

if number1 < number2 and number1 != 0:
    if number2%number1 == 0 and number2 != 0:
        print('El numero mayor ingresado es multiplo del menor')
    else:
        print('El numero mayor ingresado no es multiplo del menor')
elif number2 < number1 and number2 != 0:
    if number1%number2 == 0 and number1 != 0:
        print('El numero mayor ingresado es multiplo del menor')
    else:
        print("El numero mayor ingresado no es multiplo del menor")
