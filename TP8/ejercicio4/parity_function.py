def even (number):
    if number == 0:
        return True
    else:
        return odd(number-1)
    
def odd (number):
    if number == 0:
        return False
    else:
        return even(number-1)