
from insertion_sort_function import insertion_sort

books_list = []
while True:
    book_name = input('Ingrese el Nombre del Libro o no ingrese nada para finalizar:\n')
    if book_name == '':
        break
    else:
        
        print('Ingrese el nombre del autor:\n')
        while True:
            autor_name = input()
            if autor_name == '':
                print('Ingrese un nombre para el autor\n')
            else:
                break
        
        published_year = int(input('Ingrese el anio de publicacion:\n'))

        print('Ingrese el nombre de la Editorial:\n')
        while True:
            editorial_name = input()
            if editorial_name == '':
                print('Ingrese un nombre para la editorial\n')
            else:
                break
        
        book_dict = {book_name : [autor_name, published_year, editorial_name]}
        books_list.append(book_dict)

while True:
    sort_option = int(input('Ingrese de acuerdo a que se ordena el diccionario:\n1 - Nombre del Titulo\n2 - Autor\n3 - Fecha de Publicacion\n4 - Nombre de la Editorial'))
    if sort_option < 5 and sort_option > 0:
        break
    else:
        print('Ingrese una opcion valida')

print(insertion_sort(books_list, sort_option))