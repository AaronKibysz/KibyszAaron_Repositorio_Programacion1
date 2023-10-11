# EJERCICIO 15

factor_list = []
while True:
    number = int(input('Ingrese un numero entero positivo: '))
    if number<1:
        print('Valor invalido')
    else:
        break;

for i in range(1, number+1):
    if number%i == 0:
        factor_list.append(i)

print(f'Los divisores de {number} son:', factor_list)