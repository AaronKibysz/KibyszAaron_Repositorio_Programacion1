def sub_string_position(string, string2):
    positions = []
    str_len = len(string2)
    
    for i in range(len(string) - str_len + 1):
        if string[i:i+str_len] == string2:
            positions.append(i)
    return positions