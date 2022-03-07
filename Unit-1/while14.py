import random
pot = int(input("enter an amount of $$$$"))
max = 0
rolls = 0
while pot > 4:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls += 1
    max = rolls * 4
    if dice1 + dice2 == 7:
        pot += 4
    else:
        pot-=4
print("took", rolls, "took break you, max you couldve won was", max, "dollars")



