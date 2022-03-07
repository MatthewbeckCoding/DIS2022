weight = float(input('enter your weight'))
height = float(input('enter your height'))
bmi = weight / height * height
if bmi < 18.5:
    range = 'below'
elif bmi > 18.5 or bmi <= 24.9:
    range = 'in'

else:
    range = 'above'
print('your BMI is', bmi, 'which is', range, 'the recommended range')