students = ["peter","paul","mary"]
print(students[0])

student_ages = {}

student_ages["elliot"] = 16
student_ages["ronan"] = 17
student_ages['matthew'] = 17
student_ages['louis'] = 18
print(student_ages)

print(len(student_ages))

if "ronan" in student_ages:
    print(student_ages['ronan'])

name = input("enter a name")

if name not in student_ages:
    age = int(input("enter age"))
    student_ages[name] = age

print(student_ages)
