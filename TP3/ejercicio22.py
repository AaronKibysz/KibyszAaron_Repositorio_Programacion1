# EJERCICIO 22
even = 0
while True: 
    number = int(input('Ingrese un numero entero positivo o "-1" para FINALIZAR: '))
    if number == -1:
        break;
    elif number<-1:
        print('Ingrese un numero valido')
    else:
        addition = 0
        for i in str(number):
            addition += int(i)
        print(f'La suma de los digitos del valor ingresado es {addition}')
        if number%2 == 0:
            even += 1

print(f'La cantidad de numeros pares ingresados es {even}')