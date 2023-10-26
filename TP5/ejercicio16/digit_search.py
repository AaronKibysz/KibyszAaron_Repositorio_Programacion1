def digit_search_in_number(number, digit):
    coincidence_count = 0
    for i in str(number):
        if i == str(digit):
            coincidence_count += 1
    return coincidence_count