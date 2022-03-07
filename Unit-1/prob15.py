numbers = int(input("enter an amount of numbers"))
for i in range(1,numbers+1):
    perfectnumber = 0
    for j in range(1,i):
        if i % j == 0:
            perfectnumber += j
    if perfectnumber == i:
        print(i)
