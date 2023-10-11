# EJERCICIO 4

while True:
    number = int(input('Ingrese un numero ENTERO POSITIVO: '))
    if number>0:
        break;
    else:
        print("Numero Invalido")

for i in range(number,-1,-1):
    if i == 0:
        print(i, end='.')
    else:
        print(i, end=',')