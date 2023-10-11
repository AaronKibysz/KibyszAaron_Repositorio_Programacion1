# EJERCICIO 10

while True:
    number = int(input('Ingrese un numero Entero Positivo: '))
    if number<1:
        print("Ingrese un numero valido!!")
    else:
        break;
verificator = False
for i in range(number-1, 2,-1):
    if number%i == 0:
        verificator = True
        break;
        
if verificator == True:
    print('No es numero primo')
else:
    print('Es numero primo')