def multiple_of(n, b):
    if n == 1:
        return True
    if n % b == 0:
        return multiple_of(n // b, b)
    return False