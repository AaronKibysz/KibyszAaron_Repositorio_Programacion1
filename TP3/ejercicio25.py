# EJERCICIO 15

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


while True:
    number = int(input('Ingrese un numero entero positivo: '))
    if number < 0:
        print('No se puede calcular el factorial de un numero negativo.\nIngrese otro numero!!')
    else:
        break;

result = factorial(number)
print(f'El factorial de {number} es {result}')