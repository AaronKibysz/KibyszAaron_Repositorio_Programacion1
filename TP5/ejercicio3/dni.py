def dni_verification(dni):
    if len(str(dni)) > 8 or len(str(dni)) < 7:
        return False
    else:
        return True