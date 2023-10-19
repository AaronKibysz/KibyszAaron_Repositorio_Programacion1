### FUNCION DE SUMA DE CIFRAS

def number_addition (number):
    aux_num, number_add = 0, 0
    while number != 0:
        aux_num = number % 10
        number //= 10
        number_add += aux_num
    
    return number_add