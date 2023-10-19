### AHORCADO ###
import random
from compare_letters import compare_letter

print('---BIENVENIDO AL AHORCADO---\n')

words_tuple = ('PYTHONICO', 'LINUX', 'UBUNTU', 'ZINJAI', 'PROGRAM.H')

word_choice = random.choice(words_tuple)
tries = 0
hidden_word = []
for i in range(len(word_choice)):
    hidden_word.append('_')
hiddent_word = ''

while tries<=6:

    if hiddent_word == word_choice:
        print(f'Has adivinado la palabra, {word_choice}')
        break
    elif hidden_word != word_choice and tries>5:
        print(f'No has adivinado la palabra.\nLa palabra era {word_choice}')
        break
    hiddent_word = ''

    for i in hidden_word:
        print(i, end='')
    while True:
        letter = input('\nIngrese una letra: ')
        if len(letter) == 1:
            letter = letter.upper()
            break
        else:
            print('Ingrese una sola letra')
            for i in hidden_word:
                print(i, end='')
    if letter in word_choice:
        hidden_word = compare_letter(word_choice, hidden_word, letter)
        print('Acertaste la letra!!')
        for i in hidden_word:
            hiddent_word += i
        continue
    else:
        tries += 1
        print(f'Letra Incorrecta, quedan {6-tries} intentos')

