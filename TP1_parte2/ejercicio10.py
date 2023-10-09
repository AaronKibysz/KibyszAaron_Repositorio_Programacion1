# EJERCICIO 10

partials_marks = []
for i in range(0, 3):
    partials_marks.append(float(input('Ingrese las 3 notas de ')))

final_exam = float(input('Ingrese nota Examen Final: '))
final_project = float(input('Ingrese nota de Trabajo Final: '))

partials_addition = 0
for number in partials_marks:
    partials_addition += number

partials_addition /= 3

print('La calificacion final es: ', (partials_addition*0.55)+(final_exam*0.3)+(final_project*0.15))