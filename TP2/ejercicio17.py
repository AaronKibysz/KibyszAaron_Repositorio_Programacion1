# EJERCICIO 17

day_tuple = ('LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO')
while True:
    day_option = input('Ingrese un dia de la semana: ')
    day_option = day_option.upper()
    if not day_option in day_tuple:
        print('INGRESE UN DIA VALIDO')
    else:
        break;

if day_option == 'LUNES':
    print('Garfield odia los Lunes')
elif day_option == 'VIERNES':
    print('Aguanta al FIN DE SEMANA!!')
elif day_option == 'SABADO' or day_option == 'DOMINGO':
    print('LINDO FIN DE SEMANA')
else:
    print('Se me acabo la imaginacion')