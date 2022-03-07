numbers = int(input("enter an amount of numbers"))
total = 0
average = 0
max = -1
min = 1-1
odd = 0
even = 0
for i in range(1,numbers+1):
    num= int(input('enter a number' + str(i) + ": "))
    total += num
    if num > max:
        max = num
    if num < min:
        min = num
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

average = total/numbers
print("total", total)
print("average", average)
print("maximum", max)
print("minimum", min)
print("odd", odd)
print("even", even)

#10