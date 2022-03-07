# digits = input('enter values: ').strip()
# if digits.isdigit():
#     total = 0
#     for d in digits:
#         total = total +int(d)
#     print(total)
# else:
#     print('only enter numbers')

amount_sold = input('enter the amount you have sold').strip()
payment = 0.2
if amount_sold.isdigit():
    amount_sold = int(amount_sold)
    if amount_sold >= 10000:
        payment = amount_sold*0.10
    else:
        payment = amount_sold*0.05
    print('your commission is', '{:.2f}'.format(payment))
else:
    print('type numbers not letters')

