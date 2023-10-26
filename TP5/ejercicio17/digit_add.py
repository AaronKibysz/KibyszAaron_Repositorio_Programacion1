def digit_addition(number_list, digit):
    for number in number_list:
        digit_number = 0
        digit_coincidences = 0
        for i in str(number):
            digit_number += int(i)
            if int(i) == digit:
                digit_coincidences += 1
        print(f'La suma de los digitos del numero {number} es {digit_number} y se han encontrado {digit_coincidences} coincidencias con el digito ingresado {digit}')