# EJERCICIO 5

investment = float(input('Ingrese cuanto va a ser su inversion: '))
annual_interest = float(input('Ingrese su interes anual: %'))
annual_interest /= 100
number_of_years = int(input('Cuantos anios tendra de inversion: '))
total = 0
for i in range(1, number_of_years+1):
    capital = investment * (1 + annual_interest)
    print(f'Anio {i}: {capital:.2f}')
    investment = capital