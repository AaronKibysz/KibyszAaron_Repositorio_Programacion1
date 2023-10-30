def number_less_generator (number_list, number_gen):
    number_list2 = []
    for number in number_list:
        if number < number_gen:
            number_list2.append(number)
            print(f'El numero {number} es menor a {number_gen}, Se ha sumado a la lista')
    
    return number_list2