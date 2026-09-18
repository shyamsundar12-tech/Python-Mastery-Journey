positive_numbers = 0
negative_numbers = 0
zero_numbers = 0
for i in range(5):
    num = int(input('Enter your number:'))
    if num > 0:
        positive_numbers +=1
    elif num <0:
        negative_numbers +=1
    else:
        zero_numbers +=1
print('the positive numbers are:', positive_numbers)
print('the negative numbers are:', negative_numbers)
print('the zero numbers are:', zero_numbers)   