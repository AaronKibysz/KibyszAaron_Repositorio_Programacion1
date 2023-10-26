def words_lenght(phrase):
    words_dict = {}
    word_list = phrase.split()
    for word in word_list:
        words_dict.update({word : len(word)})
    
    return words_dict