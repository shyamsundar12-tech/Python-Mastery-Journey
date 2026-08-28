num1 = float(input('Enter first number :'))
num2 = float(input('Enter second number :'))
operator = input('Enter Operator (+,-,*,/):')
if operator == '+':
    print('Addition :',num1 + num2)
elif operator == '-':
    print('Subtraction :',num1 - num2)
elif operator == '*':
    print('multiplication :',num1 * num2)
elif operator == '/' :
    print('Divisiom :',num1 / num2)
else:
    print('Invalid! choose form the operator')

