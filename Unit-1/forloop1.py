#for loop
#count 0-10

# for i in range(11):
#     print(i)

#count 5-36 in 3s

# for i in range(5,37,3):
#     print(i)

# number = int(input('enter a number between 1 and 12'))
# if number < 1 or number > 12:
#     print('invalid')
# else:
#     for i in range(1,13):
#         print(i,'x', number,'=', i*number)

#ask user for 2 numbers add up all numbers between

# n1 = int(input('enter number1'))
# n2 = int(input('enter number2'))
# total = 0
#
# for i in range(n1, n2+1):
#     total = total + i
# print(total)

#find all multiples of 7 between 1 and 50

for x in range(0,51):
    if x % 7 == 0:
print(x)
