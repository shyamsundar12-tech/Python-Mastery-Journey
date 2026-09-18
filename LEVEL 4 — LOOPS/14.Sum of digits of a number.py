num = int(input('Enter a number:'))
total = 0
while num > 0:
    sum = num % 10
    total += sum
    num = num//10
print('The sum of digits of the number is:', total)

# intha program la user input vangi while a loop la run pandrom , user input greater than 0 va iruntha loop la run agum , 
# sum varaible la user input ah 10 la divide panni remainder ah sum variable la store pandrom ,
# num varaible la user input ah 10 la divide panni quotient ah store pandrom