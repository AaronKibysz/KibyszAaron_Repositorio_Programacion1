def number_count (number_list):
    number_list_check = []
    number_list2 = []
    for number in number_list:
        if not (number in number_list_check):
            number_tuple = (number, number_list.count(number))
            number_list2.append(number_tuple)
            number_list_check.append(number)

            
    return number_list2