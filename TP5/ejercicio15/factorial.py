def factorial_calculator(number_list):
    number_count = 0
    for number in number_list:
        number_factorial = 1
        if number == 0:
            print(f'El numero facotorial de {number} es 1')
            number_count += 1
        else:
            for i in range(1, number+1):
                number_factorial *= i
            print(f'El numero factorial de {number} es {number_factorial}')
            number_count +=1
    return number_count