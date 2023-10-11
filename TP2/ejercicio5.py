# EJERCICIO 5

chraracter = ''
while not len(chraracter)==1:
    chraracter = input('Ingrese una letra: ')
    if len(chraracter)>1:
        print('No se puede procesar el dato')
chraracter = chraracter.upper()
vocals_tuple = ('A', 'E', 'I', 'O', 'U')
if chraracter in vocals_tuple:
    print('Es Vocal')