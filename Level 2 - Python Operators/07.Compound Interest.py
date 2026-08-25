invested_amount = float(input('Enter your invested amount : '))
interest_rate = float(input('Enter the interest rate : '))
tenure = float(input('Enter the tenure : '))

total_amount = invested_amount * (1 + interest_rate/100)**tenure
compound_interest = total_amount - invested_amount

print('Total Amount : ',round(total_amount,2))
print('Compound interest : ',round(compound_interest,2))
