password = input('Enter your password')
tests = 0
correct = True
length = False
number = False
uppercase = False
lowercase = False
special = False

if not len(password[6:21]):
    correct = False
    print('Your password requires 6-20 characters')

for character in password:
    if character.isdigit():
        number = True
    ifs character.isupper():
        uppercase = False
    if character.islower():
        lowercase = True
    if not character.isalnum():
        special = True

if number == True:
    tests += 1
if uppercase == True:
    tests += 1
if lowercase == True:
    tests += 1
if special == True:
    tests += 1

if correct == True and tests >=3:
    print('your password has been accepted')
if number == False and tests <3:
        print('your password must have a number')
if uppercase == False and tests <3:
        print('your password must have an uppercase')
if lowercase == False and tests <3:
        print('your password must have a lowercase')
if special == False and tests <3:
        print('your password must have a special character')