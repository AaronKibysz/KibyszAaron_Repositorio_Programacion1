def bubble_sort (number_list):
    for i in range(len(number_list)):
        for j in range(0, len(number_list)-i-1):
            if number_list[j] > number_list[j+1]:
                number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
    
    return number_list