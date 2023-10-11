# EJERCICIO 18

salary_per_hour = float(input('Ingrese cual es su salario por hora: '))
hours_worked = float(input('Cuantas horas a trabajado? (MINIMO 48 HORAS): '))

if hours_worked<48:
    print('Se hay trabajado menos de 48 hrs, no se puede calcular el pago')
elif hours_worked == 48:
    print('El pago es de: $', hours_worked*salary_per_hour)
else:
    print('Se han trabajado', hours_worked-48, "horas extra. El pago es de: $", salary_per_hour*(48)+(salary_per_hour*1.1)*(hours_worked-48))