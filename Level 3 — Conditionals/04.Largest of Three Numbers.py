num1 = float(input('Enter Number 1 :'))
num2 = float(input('Enter Number 2 :'))
num3 = float(input('Enter Number 3 :'))

if num1 > num2 and num1 > num3:
    print('Number 1 is largest')
elif num2 > num3 and num2 > num1:
    print('Number 2 is largest') 
elif num3 > num1 and num3 > num2:
    print('Number 3 is largest')
elif num1 == num2 and num2 == num3 :
    print('Three values are same')
elif num1 == num2 and num1 > num3:
    print('Number 1 and Number 2 are largest')
elif num1 == num3 and num1 > num2:
    print('Number 1 and Number 3 are largest')
elif num2 == num3 and num2 > num1:
    print('Number 2 and Number 3 are largest')