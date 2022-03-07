speed = float(input("enter your speed"))
over = speed-100
fine = (over*5)+50
if speed <= 100:
    print('your all good')
else:
    if speed >120:
        print(fine+200)
    else:
        print(fine)