for x in range(1,101):
    if x % 3 == 0:
        print('fizz')
        if x % 5 == 0:
            print('fizzbuzz')
    elif x % 5== 0:
            print('buzz')
    else:
        print(x)
