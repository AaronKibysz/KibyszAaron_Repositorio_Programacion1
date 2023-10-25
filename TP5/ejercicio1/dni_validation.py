def dni_validation_funtion(dni):
    dni = str(dni)
    if len(dni) > 8 or len(dni) < 7:
        return False
    else:
        return True