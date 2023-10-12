# EJERCICIO 7

options = 0
while True:
    options = int(input('Ingrese una opcion\n1. MENSAJE UNO\n2. MENSAJE DOS\n3. MENSAJE TRES\n0. PARA SALIR:\n'))
    if options == 0:
        break
    elif options == 1:
        print('"La vida es un viaje que debes disfrutar a cada paso."')
    elif options == 2:
        print('"Aprovecha cada día como si fuera el último."')
    elif options == 3:
        print('"El aprendizaje es un tesoro que seguirás acumulando a lo largo de tu vida."')
    elif options>3 or options<1:
        print('Ingrese una opcion valida')

print('Los mensajes utilizados los saque de ChatGPT')