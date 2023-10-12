# EJERCICIO 4

year_list = []
for i in range(2):
        year_list.append(int(input('Ingrese un anio: ')))

for i in range(min(year_list),max(year_list)-1):
        if ((i%4 == 0 and not i%100==0) or i%400==0) and i%10 == 0:
                print(i, end=',')