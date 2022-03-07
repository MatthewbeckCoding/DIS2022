student_grades = {
    "simon": 48,
    "paul": 20,
}

for k, v in student_grades.items():
    print(k, "got:", v)

# name = input("enter a name:")
# if name in student_grades:
#     print(student_grades[name])
# else:
#     print("name not found")

print(list(student_grades.keys()))
#or
student_names = list(student_grades.keys())

print(list(student_grades.values()))

print(sorted(student_grades.keys()))

print(sorted(student_grades.values()))

print(list(reversed(sorted(student_grades.keys()))))