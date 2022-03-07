# age = int(input('enter your age: '))
#
# if age >= 18:
#     print('you can buy alcohol')
# else:
#     print('you are not old enough to buy alcohol')

# vowels = 'aeiou'
# word = input('please enter a word: ')
# last_letter = word[-1]
# if last_letter.lower() in vowels:
#     print('your word ends in a vowel')
# else:
#     print('your word ends in a consonant')

mark = input('enter your grade: ').strip()
if mark.isdigit():
    mark = int(mark)
    if mark > 100:
        print('invalid grade')
    else:
        if mark >80:
            grade = 'A'
        elif mark >70:
            grade = 'B'
        elif mark >50:
            grade ='C'
        elif mark >30:
            grade ='D'
        else:
            grade = 'E'
        print('your grade is an', grade)
else:
    print('type a number not letters')