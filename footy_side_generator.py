import random

# full list of players
players_all = [
    'Adam D', 'Alex B', 'Berki', 'Carl', 'Declan', 'Ed M', 'Elys', 'Gary L', 'George', 'Jack (Paddy)', 'Jake', 'James OG',
    'Jim', 'Josh S', 'Nathan', 'Nick', 'Oisin', 'Paddy', 'Sam', 'Stef', 'Theo', 'Victor', 'Vinny'
]

# list of available players for a given game day
players_available = [
    'Stef', 'Jim', 'Berki', 'Theo', 'Victor', 'George', 'Oisin', 'Paddy', 'Gary', 'Adam', 'Josh', 'Trevor'
]

# league leader
league_leader = 'George'

# players per side
n = 6

# selection rules
rule1 = 'carl and adam not on same team'
rule2 = 'stef and berki not on same team'
rule3 = 'at least 1 defender, 1 midfielder, 1 attacker on each team'
rule4 = 'put league leader and adam on same team'
rule5 = 'gary and adam on same team'
rule6 = 'best player and adam on same team'
rule7 = 'opposite team to adam should be average but balanced'
rule8 = 'fit players on adam team'
rule9 = 'put gary on the more unbalanced team'
rule10 = 'put guests on same team as friend'

# create team 1

team1 = random.sample(players_available, n)
print(team1)

# remaining players
players_remaining = players_available
for player in team1:
    if player in players_remaining:
        players_remaining.remove(player)

# create team 2
team2 = players_remaining
print(team2)
