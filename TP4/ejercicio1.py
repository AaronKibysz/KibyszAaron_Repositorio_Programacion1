# EJERCICIO 1

x = 0

while x <= 30:
    x += 1
    if x == 15:
        break;
    if x in [4, 6, 10]:
        print(f'The value {x} of x was skipped')
        continue
    print(f'The value of the loop is: {x}')

if 15 == x:
    print(f'The execution of the loop was broken when x was {x}')