num = int(input("enter a number"))
factor_count = 0
for x in range(2,num+1):
    if num % x == 0:
        print(x)
        factor_count += 1

if factor_count > 1:
    print(num,"not prime")
else:
    print(num,"prime")
