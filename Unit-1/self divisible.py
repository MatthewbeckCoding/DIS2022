file = open("textfiles/selfdivisibe.txt")

contents = file.readlines()

valid = True
count = 0
for line in contents:
    values = line.split()
    start = values[0]
    end = values[1]
    for i in range(start,end+1):
        x = int(values[0:i])
        d = int(values[i])
        if x % d !=0:
            valid= False
if valid == True:
    count += 1
print("amount between", start, "and", end, "is", count)