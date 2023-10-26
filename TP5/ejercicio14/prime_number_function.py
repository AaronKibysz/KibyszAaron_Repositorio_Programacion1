
def prime_number_calculator(number):
    for i in range(2, number):
        if number%i == 0:
            return True