import random

balls = []
for i in range(6):
    n = random.randint(1,45)
    while n in balls:
        n = random.randint(1,45)
    balls.append(n)

balls.sort()

print(balls)



