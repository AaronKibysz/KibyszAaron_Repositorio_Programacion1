def factorial_calculator(number_list):
    max_number = max(number_list)

    factorial_number = 1
    for i in range(1, max_number+1):
        factorial_number *= i
    return factorial_number