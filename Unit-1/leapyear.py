year = int(input('enter a year'))
leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year = True
    else:
        leap = True
print(year, leap)


