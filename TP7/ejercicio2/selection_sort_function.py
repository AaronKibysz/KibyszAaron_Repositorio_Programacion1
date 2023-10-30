def selection_sort(string_list):
    for i in range(len(string_list)):
        min_index = i
        for j in range(i+1, len(string_list)):
            if string_list[j] < string_list[min_index]:
                min_index = j
        
        string_list[i], string_list[min_index] = string_list[min_index], string_list[i]
    
    return string_list