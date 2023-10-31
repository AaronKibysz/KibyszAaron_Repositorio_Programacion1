def insertion_sort(string_list):
    for i in range(1, len(string_list)):
        string = string_list[i]
        j = i - 1
        while j >= 0 and len(string) < len(string_list[j]):
            string_list[j + 1] = string_list[j]
            j -= 1
            string_list[j + 1] = string
    
    return string_list