from student_comparator_function import student_comparator

print('\n-----Alumnos de PRIMARIA-----')
primary_list = []
while True:
    pile_name = input('\nIngrese el Nombre de Pila o "X" para dejar de aniadir alumnos:\n')
    if pile_name == 'X' or pile_name == 'x':
        print('Se dejara de agregar alumnos de primaria a la lista')
        break
    else:
        primary_list.append(pile_name)
        print(f'Se ha aniadido a {pile_name} a la lista')

print('\n-----Alumnos de SECUNDARIA-----')
secundary_list = []
while True:
    pile_name = input('\nIngrese el Nombre de Pila o "X" para dejar de aniadir alumnos:\n')
    if pile_name == 'X' or pile_name == 'x':
        print('Se dejara de agregar alumnos de secundaria a la lista')
        break
    else:
        secundary_list.append(pile_name)
        print(f'Se ha aniadido a {pile_name} a la lista')

student_comparator(primary_list, secundary_list)