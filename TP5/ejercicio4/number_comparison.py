def number_compare(number1, number2):
    if number1 > number2:
        if number1%number2 == 0:
            print('El primer numero es multiplo del segundo')
        else:
            print('El primer numero no es multiplo del segundo')
    elif number2 > number1:
        if number2%number1 == 0:
            print('El segundo numero es multiplo del primero')
        else:
            print('El segundo numero no es multiplo del primero')
    else:
        print('Ambos numeros ingresado son iguales, por lo que contaria para ser multiplos, ya queee no se toma en cuenta el propio numero y 1')