name = str(input('Enter your Name:'))
age = int(input('Enter your Age:'))
print('Enter your subjects marks:')
subject1 = float(input('Subject 1 : '))
subject2 = float(input('Subject 2 : '))
subject3 = float(input('Subject 3 : '))
subject4 = float(input('Subject 4 : '))
subject5 = float(input('Subject 5 : '))
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks/5
print('\n--------Student Report Card--------')
print('Name:',name)
print('Age:',age)
print('Total Marks:',total_marks)
print('Average Marks:',average_marks)

if average_marks >=90:
    print('Grade:A')
elif average_marks >=80:
    print('Grade:B')
elif average_marks >=70:
    print('Grade:C')
elif average_marks >=60:
    print('Grade:D')
elif average_marks >=50:
    print('Grade:E')
else:
    print('Fail')

if average_marks >=40:
    print('Result : PASS')
else:
    print('Result : FAIL')
