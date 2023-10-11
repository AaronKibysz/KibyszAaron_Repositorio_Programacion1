# EJERCICIO 12

string = input('Ingrese una palabra: ')
string = string.upper()
while True:
    word = input('Ingrese una letra: ')
    if len(word) != 1:
        print('Letra invalida, intente nuevamente')
    else:
        break;
word = word.upper()
count = string.count(word)
print(f'La letra ingresada aparece {count} veces en la palabra')