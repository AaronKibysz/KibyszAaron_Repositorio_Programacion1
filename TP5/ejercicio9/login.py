def login(user, password, tries):
    if user == 'usuario1' and password == 'asdasd':
        return True, tries
    else:
        tries += 1
        return False, tries