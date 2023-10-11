# EJERCICIO 14

a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))
if a == 0:
    print('No hay solucion ya que "a" tiene valor de 0')
elif c == 0:
    print('x1 = 0')
    print('x2 =', -(2*b)/(2*a))
else:
    cuadratic_funtion1 = (-b + (b**2-4*a*c)**(1/2))/(2*a)
    cuadratic_funtion2 = (-b - (b**2-4*a*c)**(1/2))/(2*a)
    print('x1 =', cuadratic_funtion1)
    print('x2 =', cuadratic_funtion2)