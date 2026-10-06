a = float(input('>> '))
b = float(input('>> '))
sign = input('>> ')
if sign == '+':
    print(a + b)
if sign == '-':
    print(a - b)
if sign == '*':
    print(a * b)
if sign == '/':
    try:
        print(a / b)
    except ZeroDivisionError:
        print('U cannot division by zero')
        