def word_leng_calculator(phrase):

    words = phrase.split()
    if words:
        last_word = words[-1]
        last_word_len = len(last_word)
        return last_word_len
    else:
        return 0