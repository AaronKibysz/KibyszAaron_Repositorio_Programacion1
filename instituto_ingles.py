
print('WELCOME TO THE ENGLISH INSTITUDE INTERFACE')

date = input('Ingrese el dia y la fecha con el formato Dia, DD/MM ').lower()

day = int(date[date.find(' ' )+1 : date.find('/')])
month = int(date[date.find('/')+1 :])
date = date[0 : date.find(',')]

week_list = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

if(day<1 or day>31 or month<1 or month>12 or (not(date in week_list))):
    print('Se ha producido un error')
elif(date in week_list[0:3]):
    exams_quest = input('Se han realizado examenes?: Y/N ')
    if (exams_quest == 'Y'):
        aproved = int(input('Cuantos alumnos aprobaron: '))
        desaproved = int(input('Cuantos alumnos desaprobaron: '))
        print('El procentaje de alumnos aprobados el dia de hoy es del', ((aproved*100)/(aproved+desaproved)))
elif(date == week_list[3]):
    student =int(input('Ingrese la cantidad total de alumnos: '))
    present_student = int(input('Ingrese cuantos alumnos asistieron el dia de hoy: '))
    if(present_student>(student/2)):
        print('Asistio la mayoria')
    else:
        print('No asistio la mayoria')
elif(day == 1 and (month ==1 or  month ==7)):
    print('Comienzo de nuevo ciclo')
    new_student = input('Ingrese el numero de nuevos estudiantes y aranceles en formato NA, $PA ')
    arancel_price = int(new_student[new_student.find('$') + 1 :])
    new_student = int(new_student[0: new_student.find(',')])
    print('El ingreso total es: ', (new_student*arancel_price))