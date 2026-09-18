print('========== NUMBER ANALYZER ==========')
while True:
    print('\nSelect your choice')
    print('1. Find Largest Number')
    print('2. Find Smallest Number')
    print('3. Calculate Average')
    print('4. Count Positive / Negative / Zero')
    print('5. Sum of Digits')
    print('6. Reverse a Number')
    print('7. Factorial')
    print('8. Exit')
    user_input = int(input('\nEnter your choice:'))

    if user_input ==1:
        print('\nFind the Largest Number:')
        for i in range(5):
            num = int(input('Enter a NNumber:'))
            if i == 0:
                largest = num
            else:
                if num > largest:
                  largest = num
        print('\nThe Largest Number is:',largest)

    elif user_input == 2:
        print('\nFind The Smallest Number:')
        for i in range(5):
            num = int(input('Enter your Number:'))
            if i ==0:
                smallest = num
            else:
                if num < smallest:
                    smallest = num
        print('\nThe Smallest Number is:',smallest)

    elif user_input == 3:
        print('\nCalculate Average:')
        total = 0
        for i in range(5):
            num = int(input('Enter your Number:'))
            total += num
        average = total / 5
        print('\nThe Average of 5 numbers is:',average)

    elif user_input ==4:
        print('\ncount Positive/Negative/Zero:')
        positive_count = 0
        negative_count = 0
        zero_count = 0
        for i in range(5):
            num = int(input('Enter your number:'))
            if num > 0:
                positive_count +=1
            elif num < 0:
                negative_count +=1
            else:
                zero_count +=1
        print('\nThe Positive Count is:',positive_count)
        print('The Negative Count is:',negative_count)
        print('The Zero Count is:',zero_count)

    elif user_input ==5:
        print('\nSum of Digits:')
        num = int(input('Enter your Number:'))
        total = 0
        while num >0:
            digits = num % 10
            total += digits
            num = num // 10
        print('\nThe Sum of Digits of the Number is:',total)

    elif user_input ==6:
        print('\nReverse a Number:')
        num = int(input('Enter your Number:'))
        reverse = 0
        while num > 0:
            remainder = num %10
            reverse = (reverse * 10) + remainder
            num = num // 10
        print('\nThe reverse of the Number is:',reverse)

    elif user_input == 7:
        print('\nFactorial:')
        num = int(input('Enter your Number:'))
        factorial = 1
        for i in range(1,num + 1):
            factorial *= i
        print('\nThe Factorial of the Number is:',factorial)

    elif user_input == 8:
        print('Exiting the program. Goodbye!')
        break