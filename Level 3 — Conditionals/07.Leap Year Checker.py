user = int(input('Enter your Year :'))
if  user % 400 == 0 or (user % 4 == 0 and user % 100 != 0):
    print('The Leap Year')
else :
    print('No Leap Year')