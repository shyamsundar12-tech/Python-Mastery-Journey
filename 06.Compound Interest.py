invested_amount = float(input('Enter the Invested amount:'))
interest_rate = float(input('Enter the Interest rate:'))
tenure = float(input('Enter the tenure period in years:'))

simple_interest = (invested_amount * interest_rate * tenure)/100
print('The simple interest is :',simple_interest)

Total_amount = invested_amount * (1 + interest_rate/100)**tenure 
print('The total amount is:',Total_amount)

compound_interest = Total_amount - invested_amount
print('The compound interest is:',compound_interest)

