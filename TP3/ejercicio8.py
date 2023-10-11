while True:
    number = int(input('Ingrese un numero entero Positivo: '))
    if number<0:
        print('Ingrese un numero valido!!')
    else:
        break;
string = ''
for i in range(0, number):
    number_str = str(2*i+1)
    string = number_str + ' ' + string
    print(string)