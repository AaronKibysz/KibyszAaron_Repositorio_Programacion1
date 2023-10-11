# EJERCICIO 6

while True:
    number = int(input('Cuantos niveles va a tener el triangulo: '))
    if number<1:
        print('Ingrese un numero valido')
    else:
        break;
for i in range(1,number+1):
    print(f'*'*i)