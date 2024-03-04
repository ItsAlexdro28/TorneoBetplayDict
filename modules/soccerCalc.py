teams = {}
length = 0

def teamLogin(teamName):
    teams[teamName] = {'points': 0, 'wins': 0, 'ties': 0, 'loses': 0, 'games': 0, 'favor_goals': 0, 'against_goals': 0}
    updateTeams()

def updateTeams():
    global length
    length += 1

def matchUpdate(local, visitant, score):
    if local in teams and visitant in teams:
        goals = list(map(int, score.split("-")))
        teams[local][visitant] = '-'.join(map(str, goals))
        teams[visitant][local] = '-'.join(map(str, reversed(goals)))
        reportUpdate()
    else:
        print('El nombre del equipo no está en la lista')

def reportUpdate():
    for team, data in teams.items():
        wins = 0
        ties = 0
        loses = 0
        games = 0
        favor_goal = 0
        against_goal = 0
        for opponent, score in data.items():
            if opponent != 'points':
                if score:
                    goals = list(map(int, score.split("-")))
                    if goals[0] > goals[1]:
                        wins += 1
                    elif goals[0] == goals[1]:
                        ties += 1
                    else:
                        loses += 1
                    games += 1
                    favor_goal += goals[0]
                    against_goal += goals[1]
        data['points'] = (wins * 3) + ties
        data['wins'] = wins
        data['ties'] = ties
        data['loses'] = loses
        data['games'] = games
        data['favor_goals'] = favor_goal
        data['against_goals'] = against_goal

def evalBest(n):
    if n == 1:
        best_team = max(teams.items(), key=lambda x: x[1]['games'])[0]
        return best_team, teams[best_team]['games']
    elif n == 2:
        best_team = max(teams.items(), key=lambda x: x[1]['points'])[0]
        return best_team, teams[best_team]['points']
    elif n == 3:
        best_team = max(teams.items(), key=lambda x: x[1]['wins'])[0]
        return best_team, teams[best_team]['wins']

def evalGoals(n):
    if n == 1:
        total_goals = sum([data['favor_goals'] for data in teams.values()])
        return total_goals
    elif n == 2:
        total_goals = sum([data['favor_goals'] for data in teams.values()])
        mean_goals = total_goals / len(teams)
        return mean_goals

