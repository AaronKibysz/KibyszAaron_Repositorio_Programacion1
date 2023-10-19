

def compare_letter(word, hidden_word, letter):
    for i in range(len(word)):
        if letter == word[i]:
            hidden_word[i] = letter
    return hidden_word
