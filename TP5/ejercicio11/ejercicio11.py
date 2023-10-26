# EJERCICIO 11 FUNCION PRINCIPAL

from function1 import function1
from function2 import function2

list1 = []

while True:
    number = int(input('Ingrese un numero entero, o "0" para terminar de aniadir numeros:\n'))
    if number == 0:
        break
    list1.append(number)

results = function1(function2, list1)

print(results)