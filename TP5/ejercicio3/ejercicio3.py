#EJERCICIO 3 FUNCION PRINICPAL

from name import name_verificator
from name import id_creation
from dni import dni_verification

print('Bienvenido al geenerador de IDs\n')

while True:
    name = input('Ingrese el nombre con el formato: NOMBRE APELLIDO (No ingrese nada para finalizar):\n')
    if len(name) == 0:
        break;
    name_ver = name_verificator(name)
    if name_ver == 1:
        print('Ingrese al menos 2 palabras que corresponan al nombre y apellido')
        continue
    elif name_ver > 3:
        print('No puede ingresar mas de 3 palabras, ya que si se colocan 3 pertenecen a NOMBRE NOMBRE2 APELLIDO y se tomara asi')
        continue
    else:
        while True:
            dni = int(input('Ingrese su DNI (ENTRE 7 u 8 DIGITOS): \n'))
            dni_ver = dni_verification(dni)
            if dni_ver == False:
                print('Debe ingresar un DNI valido')
                continue
            else:
                break

        id = id_creation(name, dni)
        print(f'El id del usuario {name} es: {id}')

print('\nPrograma Finalizado')