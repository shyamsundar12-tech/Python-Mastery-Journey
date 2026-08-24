principle = float(input('Enter the principle amount:'))
rate = float(input('Enter the rate of interest:'))
tenure = float(input('Enter the tenure in years:'))

simple_interest = (principle * rate * tenure)/100
print('The simple interest is :', simple_interest)

total_amount = principle + simple_interest
print('The total amount after', tenure, 'years is :', total_amount)