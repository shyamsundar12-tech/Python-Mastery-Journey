user = input('Enter your password :')

if len(user) < 6:
    print('Weak Password')
elif len(user) < 10:
    print('Medium Password')
else :
    print('Strong Password')