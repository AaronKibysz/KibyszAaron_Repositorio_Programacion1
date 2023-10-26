# EJERCICIO 12 FUNCION PRINCIPAL

from words import words_lenght

phrase = input('Ingrese una frase:\n')
words_dict = words_lenght(phrase)
for word, len_ in words_dict.items():
    print(f'La palabra {word} tiene {len_} letras')