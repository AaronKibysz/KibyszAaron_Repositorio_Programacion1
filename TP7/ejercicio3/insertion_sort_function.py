def insertion_sort (books_list, sort_option):
    if sort_option == 1:
        for i in range(1, len(books_list)):
            actual_book = books_list[i]
            j = i - 1
            while j >= 0 and list(actual_book.keys())[0] < list(books_list[j].keys())[0]:
                books_list[j + 1] = books_list[j]
                j -= 1
            books_list[j + 1] = actual_book
    elif sort_option > 1 and sort_option < 5:
        for i in range(1, len(books_list)):
            actual_book = books_list[i]
            j = i - 1
            camp_order = list(actual_book.keys())[sort_option - 2]
            while j >= 0 and actual_book[camp_order] < books_list[j][camp_order]:
                books_list[j + 1] = books_list[j]
                j -= 1
            books_list[j + 1] = actual_book

    return books_list