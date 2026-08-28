user_input = input('Enter user Name : ')
password = input('Enter your Password : ')
correct_user = 'shyam'
correct_password ='1234'
if user_input == correct_user and password == correct_password:
    print('Login Successful')
else:
    print('Invalid username or password , Try Again')