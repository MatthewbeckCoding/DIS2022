import random
over = 0
under = 0
craps = 0
rolls = int(input("enter a number of rolls"))
for x in range(rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    if total > 7:
        print("over")
    elif total< 7:
        print("under")
    else:
        print("craps")
print(rolls)