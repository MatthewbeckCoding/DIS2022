import random
def check_for_winner(a,b):
    rock = 0
    paper = 1
    scissors = 2
    spock = 3
    lizard = 4
    d = (5 + a - b) % 5
    if d == 1 or d == 3:
        winner = "player"
    elif d == 2 or d == 4:
        winner = "computer"
    elif d == 0:
        winner = "tie"

    return winner


totalplayer = 0
totalcomputer = 0
while totalplayer < 3 or totalcomputer < 3:
    a = input("enter: ")
    b = random.randint(0, 4)
    r = check_for_winner(a, b)
    if r == "player":
        totalplayer += 1
    elif r == "computer":
        totalcomputer += 1
    print(r)
if totalplayer == 3:
    tr = "play"
elif totalcomputer == 3:
    tr = "comp"
print(tr)

