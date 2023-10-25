# EJERCICIO 1 FUNCION MAIN

from dni_validation import dni_validation_funtion

dni = int(input('Ingrese su numero de DNI: '))
dni_validation = dni_validation_funtion(dni)

print(dni_validation)