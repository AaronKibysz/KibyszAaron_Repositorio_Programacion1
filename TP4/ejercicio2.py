# EJERCICIO 2

addition = 0

while True:
    log = input('Ingrese la operacion con el formato D/R $$$\n(D es deposito, R es Retirar):\n')
    if not log:
        break
    log = log.upper()
    if log.startswith('D'):
        addition += int(log.split()[-1])
    elif log.startswith('R'):
        addition -= int(log.split()[-1])
    else:
        print('Operacion invalida')

print(f'El final de la operacion es {addition}')