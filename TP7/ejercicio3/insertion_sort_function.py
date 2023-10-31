def insertion_sort(books_list, sort_option):
    for i in range(1, len(books_list)):
        actual_book = books_list[i]
        j = i - 1
        while j >= 0 and actual_book[sort_option] < books_list[j][sort_option]:
            books_list[j + 1] = books_list[j]
            j -= 1
        books_list[j + 1] = actual_book

    return books_list