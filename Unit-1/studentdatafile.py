filename = "textfiles/studentdata.txt"
file = open(filename)
contents = file.readlines()

for line in contents:
    values = line.split(',')
    name = values[0].pop
    total = 0
    for i in range(len(values)):
        total+= int(values[i])
    average = total/len(values)
    print(name, len(values), average)