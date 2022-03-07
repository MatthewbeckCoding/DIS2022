date= input('enter a year in dd/mm/yy')
day = int(date[:2])
month = int(date[3:5])
year = int(date[-2:])

if day * month == year:
    print('this is a magic year')
else:
    print('this is not a magic year')