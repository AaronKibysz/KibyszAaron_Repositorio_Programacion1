# EJERCICIO 21

km_per_lt = int(input('Cuantos kilometros puede recorrer por cada litro?: '))
tank = int(input('Cual es la capacidad en litros del tanque?: '))
total_km = int(input('Cuantos kilometros se recorreran?: '))

print('La cantidad de tanques de combustible necesarios son: ',(total_km/km_per_lt)/tank)