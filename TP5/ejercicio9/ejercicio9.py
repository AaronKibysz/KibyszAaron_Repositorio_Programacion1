# EJERCICIO 9 FUNCION PRINCIPAL

from login import login

tries = 0
while tries < 3:
    user = input('Ingrese el nombre de usuario:\n')
    password = input('Ingrese la contrasenia:\n')
    verification, tries = login(user, password, tries)
    if verification == True:
        print('Se ha ingresado correctamente')
        break

if tries == 3:
    print('Demasiados intentos incorrectos')