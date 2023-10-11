# EJERCICIO 3

while True:
    number = int(input('Ingrese un numero ENTERO POSITIVO: '))
    if number>0:
        break;
    else:
        print("Numero Invalido")

for i in range(1,number, 2):
    if i == number or i== number-1:
        print(i, end='.')
    else:
        print(i, end=',')