# Ejercicio Practico del Primer Parcial

print('Bienvenido al Programa de Juegos')
name = input('Ingrese su nombre: ')

while True: # Ocupe este ciclo while, para cuando se cumpla la condicion de salida, deje de ejecutarse
    option = input(f'{name}, Ingrese que tipo de juego quiere:\nJuego de Numeros (N)\nJuego de Palabras (P)\n')
    option = option[0].upper() # Para comparar solo letras mayusculas y prevenir el error, ademas se busca en el primer caracter del str en caso que se introduzca por accidente 'numeros' o 'palabras
    if option == 'N' or option == 'P':
        break;
    print(f'Ingrese una opcion valida {name}')

if option == 'N': # Codicicinal 'if' y 'elif' para ejercutar una opcion o otra, de acuerdo a lo elejido anteriormente
    number_list = [] # Lista para guardas todos los numeros ingresados
    while True:
        number = int(input(f'{name}, Ingrese un numero entero o "0" para finalizar:\n'))
        if number == 0:
            break
        else:
            number_list.append(number) # Aca se cargan en la lista los numeros ingresados, excepto el '0' 
    
    even_max = min(number_list) # Seteo esta variable en el valor minimo, ya que en caso que solo se ingrese 1 valor, este sera el mayor si o si, y en caso que no, se sobreescribira con el mayor
    odd_addition = 0
    odd_count = 0
    for i in number_list: # Aca analizar cada numero de la lista, y si cumple una de las condiciones de numero, realiza una accion u otra
        if i%2 == 0 and i>even_max:
            even_max = i
        elif i%2 != 0:
            odd_addition += i
            odd_count += 1
    if even_max%2 == 0:
        print(f'El mayor numero par ingresado por {name} es: {even_max}')
    else:
        print(f'No se han ingresado numeros pares por {name}') # Esta linea solo se ejecuta en caso que no se haya ingresado ningun numero par
    print(f'El promedio de los numeros impares ingresados por {name} es: {odd_addition/odd_count}')
elif option == 'P':
    vocals_tupple = ('A', 'E', 'I', 'O', 'U') # Se creo una tupla con cada vocal para que se analice si la letra pertenece a la tupla
    vocals_count = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0} # Y se creo este diccionario para que guarde la clave(vocal) y el cuantas hay de cada uno
    phrase = input('Ingrese una frase: ')
    for letter in phrase.upper(): # Aca se analiza letra por letra de la frase ingresada y se settea como mayuscula, para que a la hora de comparar no salte ningun error
        if letter in vocals_tupple:
            vocals_count[letter] += 1
    
    print(f'En la frase que ha ingresado {name}, se han contados estas volcales: ') 
    for letter, count in vocals_count.items(): # Imprime todas las claves y sus valores
        print(f'{letter}: {count}')