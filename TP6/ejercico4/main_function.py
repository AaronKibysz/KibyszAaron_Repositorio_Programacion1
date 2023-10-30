
from ficture_function import *

teams_list = []
for i in range(10):
    team_goals = []
    for j in range(10):
        if i != j:
            while True:
                goals = int(input(f'Ingrese la cantidad de goles del equipo {i+1} contra el equipo {j+1}:\n'))
                if goals < -1:
                    print('La cantidad de goles ingresada es invalida, ingrese un valor valido\n')
                else:
                    team_goals.append(goals)
                    break
        else:
            team_goals.append(0)
    teams_list.append(team_goals)

teams_print(teams_list)

teams_results(teams_list)

goals_diference(teams_list)

teams_points = team_points_count(teams_list)

print('\n\nCantidad de Puntos por Equipo\n')
for team, points in teams_points.items():
    print(f'Equipo {team}: {points}')