# name = input("enter a name or 'QUIT' to exit: ")
#
# while name != "QUIT":
#     print(name)
#     name = input("enter a name: ")

# n = int(input("enter a number"))
# total = 1
# i = 1
# while i <= n:
#     total = total*i
#     i += 1
# print(total)

n = int(input("enter a number"))

while n != 1:
    print(n)
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = n * 3 + 1
print(n)
