name = input('Enter your name :')

mark1 = int(input('Enter your First subject marks :'))
mark2 = int(input('Enter your Second subject marks :'))
mark3 = int(input('Enter your Third subject marks :'))
mark4 = int(input('Enter your Forth subject marks :'))
mark5 = int(input('Enter your Fifth subject marks :'))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
percentage = (total/500)*100

print('\nName :',name)
print('Total Mark :',total)
print('Average :',average)
print('Percentage :',round(percentage,2),'%')
if mark1 >=40 and mark2 >=40 and mark3 >=40 and mark4 >= 40 and mark5 >= 40:
  if percentage >=90:
    print('Grade:A')
  elif percentage >= 80:
    print('Grade:B')
  elif percentage >= 70:
    print('Grade:C')
  elif percentage >= 60:
    print('Grade:D')
  elif percentage >=50:
    print('Grade:E')
  else:
    print('FAIL')
else:
  print('Fail')