# EJERCICIO 6
number_list = []
for i in range(0, 3):
    number_list.append(float(input('ingrese un numero')))
addition = 0
for number in number_list:
    addition += number

print(addition)