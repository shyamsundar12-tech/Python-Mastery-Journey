for i in range(5):
    num = int(input('Enter your number:'))
    if i==0:
        smallest = num # intha place la if i == 0 nu input values store pannikirom , first number ah smallest variable la store pannirukkom.
    else:
        if num < smallest:
            smallest = num
print('The smallest number is:', smallest)