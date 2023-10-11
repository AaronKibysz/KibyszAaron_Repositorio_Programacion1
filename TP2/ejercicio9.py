# EJERCICIO 9

women_tuple = ('A','B','C','D','E','F','G','H','I','J','K','L')
men_tuple = ('O','P','Q','R','S','T','U','V','W','X','Y','Z')
name = input('Ingrese su nombre: ')
name = name.upper()
genre = input('Ingrese su genero: HOMBRE/MUJER: ')
genre = genre.upper()

if genre == 'HOMBRE':
    if name[0] in men_tuple:
        print('Pertenece al grupo A')
    else:
        print('Pertenece al grupo B')
elif genre == 'MUJER':
    if name[0] in women_tuple:
        print('Pertenece al grupo A')
    else:
        print('Pertenece al grupo B')
else:
    print("No se ha ingresado un genero valido")