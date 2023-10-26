# EJERCICIO 10 FUNCION PRINCIPAL

from discount import discount_calculator

products_dict = {}

try:
    while True:

        product_value = input('Ingrese el valor del producto:\n')
        if product_value == '':
            break
        product_value = float(product_value)
        if product_value < 0:
            print('Ingrese un numero valido')
            continue

        while True:
            discount_value = float(input('Ingrese el valor del descuento:\n'))
            if discount_value < 0 or discount_value > 100:
                print('Ingrese un numero de descuento valido')
            else:
                break
        
        products_dict.update({product_value : discount_value})
except ValueError:
    print('Ingreso invalido, Ingrese un valor valido')

print(f'\nEl precio final de la compra es: ${discount_calculator(products_dict)}')