# EJERCICIO 10

age = int(input('Ingrese la edad: '))
if age<0:
    print('Edad Invalida')
elif age<4:
    print('Puede entrar Gratis')
elif age<18:
    print('Debe pagar $500')
else:
    print('Debe pagar $1000')