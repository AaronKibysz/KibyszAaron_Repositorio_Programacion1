# EJERCICIO 9

password = input('Ingrese una contrasenia: ')
print('Confirme la contrasenia: ')
while True:
    confirm_password = input()
    if password != confirm_password:
        print("Contrasenia incorrecta\nIntente Nuevamente:", end=' ')
    else:
        break;