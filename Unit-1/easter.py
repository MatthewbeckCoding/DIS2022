year = int(input('enter a year'))


if year <1982 or year > 2048:
    print('error invalid year')
else:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    easter = 22 + d + e
    if easter >31:
        easter = easter-31
        print('april', easter)
    else:
        print('march', easter)

