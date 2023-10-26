# EJERCICIO 6 FUNCION PRINCIPAL
from separator import separator_funtion

print('SEPARADOR DE CARACTERES\n')

while True:
    text = input('Ingrese un texto:\n')
    if len(text) > 0:
        break
    else:
        print('Ingrese un texto de al menos 1 caracter')

print(f'El texto resultado es:\n{separator_funtion(text)}')