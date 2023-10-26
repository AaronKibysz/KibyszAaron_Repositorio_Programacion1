# EJERCICIO 13 FUNCION PRINCIPAL

from module_function import module_calculator

vector_parameters = []

for i in range(3):
    parameter = float(input(f'Ingrese el valor del parametro {i+1}: \n'))
    vector_parameters.append(parameter)

print(f'El modulo del vector {vector_parameters} es {module_calculator(vector_parameters)}')