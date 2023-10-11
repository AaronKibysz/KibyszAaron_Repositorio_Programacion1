# EJERCICIO 11
pizza_ing = ['MOZZARELLA', 'TOMATE']
veg_option = input('Quiere una Pizza Vegetariana Y/N: ')
veg_option = veg_option.upper()
if veg_option == 'Y':
    opt_ing_veg = input('Puede elegir Para agregar un ingrediente de los siguientes: Pimiento o Tofu (Ninguno si no quiere sumar ingrediente): ')
    opt_ing_veg = opt_ing_veg.upper()
    if opt_ing_veg == 'PIMIENTO' or opt_ing_veg == 'TOFU':
        pizza_ing.append(opt_ing_veg)
    print('La pizza elegida es Vegetariana')
    print('Los ingredientes de la pizza van a ser: ', pizza_ing)
elif veg_option == 'N':
    opt_ing_noveg = input('Puede elegir Para agregar un ingrediente de los siguientes: Peperoni, Jamon o Salmon (Ninguno si no quiere sumar ingredientes): ')
    opt_ing_noveg = opt_ing_noveg.upper()
    if opt_ing_noveg == 'PEPERONI' or opt_ing_noveg == 'JAMON' or opt_ing_noveg == 'SALMON':
        pizza_ing.append(opt_ing_noveg)
    print('La pizza elegida es NO vegetaria')
    print('Los ingredientes de la pizza van a ser: ', pizza_ing)
else:
    print('No se ingresado una opcion valida')
