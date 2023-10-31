
from insertion_sort_function import insertion_sort

books_list = []
while True:
    book_name = input('\nIngrese el Nombre del Libro o no ingrese nada para finalizar:\n')
    if book_name == '':
        break
    else:
        
        print('\nIngrese el nombre del autor:')
        while True:
            autor_name = input()
            if autor_name == '':
                print('\nIngrese un nombre para el autor\n')
            else:
                break
        
        published_year = int(input('\nIngrese el anio de publicacion:\n'))

        print('\nIngrese el nombre de la Editorial:')
        while True:
            editorial_name = input()
            if editorial_name == '':
                print('\nIngrese un nombre para la editorial\n')
            else:
                break
        
        book_dict = {'title': book_name, 'author': autor_name, 'year': published_year, 'editorial' : editorial_name}
        books_list.append(book_dict)

while True:
    sort_option = int(input('Ingrese de acuerdo a que se ordena el diccionario:\n1 - Nombre del Titulo\n2 - Autor\n3 - Fecha de Publicacion\n4 - Nombre de la Editorial'))
    if sort_option < 5 and sort_option > 0:
        if sort_option == 1:
            sort_option = 'title'
        elif sort_option == 2:
            sort_option = 'author'
        elif sort_option == 3:
            sort_option = 'year'
        else:
            sort_option = 'editorial'
        break
    else:
        print('Ingrese una opcion valida')

sorted_books = insertion_sort(books_list, sort_option)
print(sorted_books)