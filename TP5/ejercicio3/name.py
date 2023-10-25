def name_verificator(name):
    name_words = name.split()
    return len(name_words)

def id_creation(name, dni):
    name_words = name.split()
    id = name_words[0] + str(len(name_words[-1])) + str(dni)[0:3]
    return id