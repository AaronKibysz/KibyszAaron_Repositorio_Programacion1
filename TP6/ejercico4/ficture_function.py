def teams_print (teams_list):
    print('---RESUMEN GOLES---\n')
    for index_team, team in enumerate(teams_list):
        print(f'Equipo {index_team+1}: ', end=' ')
        for goals_mount in team:
            print(goals_mount, end=' ')
        print('')

def teams_results(teams_list):
    for index_teams, team in enumerate(teams_list):
        victory_count = 0
        losses_count = 0
        draw_count = 0
        for index_goals in range(len(team)):
            if index_teams != index_goals:
                if teams_list[index_teams][index_goals] == teams_list[index_goals][index_teams]:
                    draw_count += 1
                elif teams_list[index_teams][index_goals] < teams_list[index_goals][index_teams]:
                    losses_count += 1
                else:
                    victory_count += 1
        print(f'\n\nEQUIPO {index_teams + 1}\n\nVictorias: {victory_count}\nDerrotas: {losses_count}\nEmpates: {draw_count}')

def goals_diference (teams_list):
    goals_dicc = {}
    for index_teams, team in enumerate(teams_list):
        goals_results = []
        favor_goals = sum(team)
        agains_goals = 0
        for index_goals in range(len(team)):
            agains_goals += teams_list[index_goals][index_teams]
        
        print(f'\n\nEquipo {index_teams+1}\n\nGoles a Favor: {favor_goals}\nGoles Recibidos: {agains_goals}\nResumen Goles: {favor_goals-agains_goals}')

def team_points_count(teams_list):
    teams_points_dicc = {}
    for index_teams, team in enumerate(teams_list):
        team_points = 0
        victory_count = 0
        draw_count = 0
        for index_goals in range(len(team)):
            if index_teams != index_goals:
                if teams_list[index_teams][index_goals] == teams_list[index_goals][index_teams]:
                    draw_count += 1
                elif teams_list[index_teams][index_goals] > teams_list[index_goals][index_teams]:
                    victory_count += 1
        team_points = victory_count*3 + draw_count
        teams_points_dicc[index_teams+1] = team_points
    
    return teams_points_dicc