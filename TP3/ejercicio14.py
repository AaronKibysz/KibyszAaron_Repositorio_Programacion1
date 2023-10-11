# EJERCICIO 14

even_list = []
odd_list = []
number1 = int(input('Ingrese el primer numero: '))
number2 = int(input('Ingrese el segundo numero: '))
if number1 < number2:
    for i in range(number1, number2):
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
else:
    for i in range(number2, number1):
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

print('Los numeros pares entre ambos numeros son:', even_list)
print('Los numeros impares entre ambos numeros son:', odd_list)