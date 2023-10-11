# EJERCICIO 4

option = input('Ingrese que candidato quiere votar (A, B o C): ')
options_dict = {'A':'Partido Rojo', 'B':'Partido Verdad', 'C':'Partido Azul'}
try:
    if option in options_dict:
        print('Usted ha votado al',options_dict[option])
    else:
        print('Opcion Incorrecta')
except Exception as e:
    print('')