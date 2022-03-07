# pop = 26
# years = 0
#
# while pop < 50:
#     pop = pop + (pop*0.03)
#     years+=1
# print(years)

num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))
if num1 >= num2:
    ln = num1
    sn = num2
else:
    ln = num2
    sn = num1

while sn != 0:
    remainder = ln % sn
    ln = sn
    sn = remainder

print(ln)

