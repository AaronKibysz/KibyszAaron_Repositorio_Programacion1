# EJERCICIO 20

marks_list = []
for i in range(4):
    while True:
        number = float(input('Ingrese nota: '))
        if number>10 or number<1:
            print('Ingrese una nota valida (entre 1 y 10)')
        else:
            marks_list.append(number)
            break;

if sum(marks_list)/len(marks_list) < 6:
    print('Ha desaprobado')
else:
    print('Ha aprobado')