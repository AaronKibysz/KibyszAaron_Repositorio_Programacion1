#EJERCICIO 1

abc_tuple = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z')

corrimiento = int(input('Ingrese el numero del corrimiento: '))

message_list = []
for i in range(5):
    message_list.append(input('Ingrese mensaje '))
    message_list[i] = message_list[i].upper()

for i in range(len(message_list)):
    message_aux = message_list[i]
    message_aux2 = ''
    
    for letter in message_aux:
        if letter not in abc_tuple:
            message_aux2 += letter
        else:
            index = abc_tuple.index(letter)
            new_index = (index + corrimiento) % len(abc_tuple)
            message_aux2 +=  abc_tuple[new_index]
    print(message_aux2)

#EJERCICIO 2

number_list = []
print('Ingrese numeros enteros positivos o 0 para finalizar')
x = -1
while x < 0 or x>0:
    number_element = int(input())
    if number_element == 0:
        break
    elif number_element < 0:
        continue
    else:
        number_list.append(str(number_element))

even = 0
not_even = 0;
for element in range(len(number_list)):
    even2 = 0
    not_even2 = 0
    for number_digit in number_list[element]:
        if int(number_digit)%2 == 0:
            even += 1
            even2 += 1
        else:
            not_even += 1
            not_even2 += 1
    print('El numero ingresado', number_list[element], ' Tiene ', even2, " Cifras Pares y ", not_even2, ' Cifras Impares')

print('Se han ingresado : ', even, 'Cifras Pares en Total')
print('Se han ingresado : ', not_even, 'Cifras Impares en Total')