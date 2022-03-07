students = []

students.append("peter")
students.append("paul")
students.append("mary")
print(type(students))
print(students)
print(students[1])
print(len(students))
print(students[-1])

for student in students:
    print(student)

students.append("jake")
print(students)

students.sort()
print(students)
students.reverse()
print(students)

students.pop()
print(students)

students.remove('peter')
print(students)

new_students = ["simon","andrew","martha","andrea"]
grades = [23,45,79,32]

for i in range(len(new_students)):
    print(new_students[i],"got the grade",grades[i])

name = "matthew"
letters = list(name)
print(letters)

name = "Matthew Beck"
name_parts = name.split()
print(name_parts)

first_name = name_parts[0]
last_name = name_parts[1]
print(last_name.upper(),first_name)