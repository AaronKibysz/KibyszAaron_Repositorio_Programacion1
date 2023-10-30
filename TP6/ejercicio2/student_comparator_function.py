def student_comparator(primary_list, secundary_list):
    check_list = []
    for student in primary_list:
        if not student in check_list:
            if student in secundary_list:
                check_list.append(student)
    
    print('\n---Lista de Alumnos de Primaria---\n')
    for student in primary_list:
        print(f'Alumno: {student}')
    
    print('\n---Lista de ALumnos de Secundaria(Sin Repeticiones respecto a los de Primaria)---\n')
    for student in secundary_list:
        if not student in check_list:
            print(f'Alumno: {student}')
    
    print('\n---Lista de alumnos repetidos en Ambas Listas---\n')
    for student in check_list:
        print(f'Alumno: {student}')

    print('\n---Lista de Alumnos de Primario que no se repiten en secundario---\n')
    for student in primary_list:
        if not student in check_list:
            print(f'Alumno: {student}')