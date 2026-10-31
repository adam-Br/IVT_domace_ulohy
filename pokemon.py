import json
with open('effectiveness.json') as json_file:
    data = json.load(json_file)


def remake_chart():
    global data
    strength_to_num={"super effective":2, "normal effective":1, "not very effective": 0.5, "no effect":0}
    data_changed = {}

    for strength in data:
        for attacker in data[strength]:
            if attacker not in data_changed.keys():
                data_changed[attacker] = {}
            for defender in data[strength][attacker]:
                data_changed[attacker][defender] = strength_to_num[strength]
    return data_changed

def battle(attacker,defender,power,opponent_power):
    global data_changed
    attacker_split = attacker.split(" ")
    defender_split = defender.split(" ")

    if len(attacker_split) == 2 and len(defender_split) == 2:
        utok1 =data_changed[attacker_split[0]][defender_split[0]] * data_changed[attacker_split[0]][defender_split[1]]
        utok2 =data_changed[attacker_split[1]][defender_split[0]] * data_changed[attacker_split[1]][defender_split[1]]
        return max(utok1,utok2)
    elif len(attacker_split) == 2 and len(defender_split) == 1:
        return max(data_changed[attacker_split[0]][defender_split[0]],data_changed[attacker_split[1]][defender_split[0]])
    elif len(attacker_split) == 1 and len(defender_split) == 1:
        return data_changed[attacker_split[0]][defender_split[0]]
    elif len(attacker_split) == 1 and len(defender_split) == 2:
        return data_changed[attacker_split[0]][defender_split[0]] * data_changed[attacker_split[0]][defender_split[1]]
    return None

def attack(p1:int,p2:int, army:str)->tuple:
    army_f = army.split(",")
    army1= army_f[:p1]
    army2= army_f[p1:]

    my_power = 0.0
    opponent_power = 0.0

    for attacker in army1:
        for defender in army2:
            my_power += battle(attacker,defender,my_power,opponent_power)
    for defender in army2:
        for attacker in army1:
            opponent_power += battle(defender, attacker,opponent_power,my_power)
    if my_power > opponent_power:
        return (my_power,opponent_power,"ME")
    elif my_power < opponent_power:
        return (my_power,opponent_power,"THEM")
    elif my_power == opponent_power:
        return (my_power,opponent_power,"TIE")
#Main code:
data_changed = remake_chart()
my_pkm = input("Your team size: ")
their_pkm = input("Opponent team size: ")
pokemon = input("Pokemon types: ")
result = attack(2,6,pokemon)
print(result)


