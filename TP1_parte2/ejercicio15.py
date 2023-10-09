# EJERCICIO 15

HH = int(input('Ingrese el numero de Hora de Salida: '))
MM = int(input('Ingrese el numero de Minutos de Salida: '))
SS = int(input('Ingrese el numero de Segundos de Salida: '))
T = int(input('Ingrese cuantos segundos se tardara en llegar al destino: '))

HH += T//3600
MM += (T%3600)//60
SS += ((T%3600)%60)
days = 0
while SS > 59:
    MM += 1
    SS -= 60
    while MM > 59:
        HH +=1
        MM -= 60
        while HH>23:
            days += 1
            HH -= 24
if days == 0:
    print('El horario de llegada va a ser a las: ',HH,'hrs, ',MM,'min, ',SS,'seg.')
else:
    print('El horario de llegada va a ser a las: ', HH, 'hrs, ',MM,'min, ',SS,'seg. de ',days,' dias siguientes')