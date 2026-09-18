

for i in range(5):
    num = int(input("Enter a number: "))
    if i == 0:
        largest = num # intha place la if i == 0 nu input values store pannikirom , first number ah largest variable la store pannirukkom.
    else:
        if num > largest:
            largest = num
print("The largest number is:", largest)  