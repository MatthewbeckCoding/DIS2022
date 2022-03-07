filename = "textfiles/results.txt"

file = open(filename)

contents = file.readlines()
# noA = 0
# noB = 0
# noC = 0
# noF = 0
names = []
marks = []

for i in range(1,len(contents)+1):
    if i % 2 == 0:
        marks.append(i)
    else:
        names.append(i)
for i in range(len(names)):
    name = names[i]
    mark = marks[i]
    if mark >= 80:
        grade = 'A'
        #noA += 1
    elif mark >= 70:
        grade = 'B'
        #noB += 1
    elif mark >= 50:
        grade = 'C'
        #noC += 1
    else:
        grade = 'F'
        #noF += 1
    print(name, mark, grade)
    # print("summary")
    # print("As",noA)
    # print("Bs", noB)
    # print("Cs", noC)
    # print("Fs", noF)
