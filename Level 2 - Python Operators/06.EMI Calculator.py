loan_amount = float(input('Enter your Loan Amount : '))
interest_rate = float(input('interest : '))
Tenure = float(input('Enter the period of loan : '))

monthly_rate =  (interest_rate/12)/100
number_of_month = Tenure * 12

emi = loan_amount * monthly_rate * (1 + monthly_rate) ** number_of_month / ((1 + monthly_rate) ** number_of_month -1)

print('EMI : ',emi)
print('Monthly Rate : ',(round(monthly_rate,2)))
print('Number of Month : ',number_of_month)

