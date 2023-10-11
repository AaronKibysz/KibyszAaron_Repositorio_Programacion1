# EJERCICIO 20

addition = 0
while True:
    number = int(input('Ingrese numeros enteros. INGRESE 0 PARA FINALIZAR: '))
    if number != 0:
        addition += number
    else:
        break;

print(f'La sumatoria de los numeros ingresados es {addition}')