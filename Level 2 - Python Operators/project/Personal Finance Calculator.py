print('======PERSONAL FINANCE CALCULATOR======')
while True:
  print('\nSelect your choice!')
  print('1.Basic Calculator :')
  print('2.Profit & loss Calculator : ')
  print('3.Percentage Calculator :')
  print('4.Simple Interest Calculator :')
  print('5.Compund Interest Calculator :')
  print('6.EMI Calculator :')
  print('7.Shopping Calculator :')
  print('8.Exit')
  user_input = int(input('\nEnter your choice : ')) 

  if user_input == 1:
   print('\nBasic Calculator : ')
   num1 = float(input('\nEnter your first number :'))
   num2 = float(input('Enter your second number :'))
   addition = (num1 + num2)
   subtraction = (num1 - num2)
   multiplication = (num1 * num2)
   division = (num1 / num2)
   print('Addition :',addition)
   print('Subtraction :',subtraction)
   print('Multiplication :',multiplication)
   print('Division :',division)

  elif user_input == 2:
    print('\nProfit & loss calculator :')
    cost_price = float(input('\nEnter your cost price :'))
    selling_price = float(input('Enter your selling price :'))
    if cost_price < selling_price:
      profit = selling_price - cost_price
      print('PROFIT')
      print('Profit Amount',profit)
    else :
      loss = cost_price - selling_price
      print('LOSS')
      print('Loss Amount',loss)

  elif user_input == 3:
    print('\nPercentage Calculator :')
    obtained_marks = float(input('\nEnter your obtained marks :'))
    total_marks = float(input('Enter the Total Marks :'))
    marks = (obtained_marks/total_marks)*100
    print('Your Percentage is :',round(marks,2),'%')

  elif user_input == 4:
    print('\nSimple Interest Calculator :')
    principle = float(input('\nEnter your Principle Amount :'))
    rate = float(input('Enter the rate of interest :'))
    tenure = float(input('Enter the in years : ') )
    simple_interest = (principle * rate * tenure)/100
    print('Simple Interest :',round(simple_interest,2))
    total_amount = principle + simple_interest
    print('The Total Amount after',tenure,'Year is :',total_amount)

  elif user_input == 5:
    print('\nCompound Interest Calculator :')
    invested_amount = float(input("\nEnter your Invested Amount :"))
    interest_rate = float(input('Enter the Interest Rate :'))
    tenure = float(input('Enter the Tenure :'))
    total_amount = invested_amount * (1+ interest_rate/100)**tenure
    compound_interest = total_amount - invested_amount
    print('\nTotal Amount :',round(total_amount,2))
    print('Compound Interest :',round(compound_interest,2))

  elif user_input == 6:
    print('\nEMI Calculator :')
    loan_amount = float(input('\nEnter your Loan Amount :' ))
    interest_rate = float(input('Enter the interest of loan :'))
    tenure = float(input('Enter the period od loan :'))
    monthly_rate = (interest_rate/12)/100
    number_of_month = tenure *12
    emi = loan_amount * monthly_rate * (1 + monthly_rate) ** number_of_month / ((1 + monthly_rate)** number_of_month - 1)
    print('\nEMI :',round(emi,2))
    print('Monthly Rate :',round(monthly_rate,2))
    print('Number of Month :',number_of_month)

  elif user_input == 7:
    print('\nShopping Discount :')
    amount =  float(input('\nEnter the Amount :'))
    if amount < 1000:
      discount = 0
    elif amount < 5000:
      discount = 5
    elif amount < 10000:
      discount = 10
    elif amount < 15000:
      discount = 15
    elif amount < 20000:
      discount = 20
    else :
      discount = 30

    discount_rate = amount * discount / 100
    final_amount = amount - discount_rate
    print('\nOriginal Amount :',amount)
    print('Discount Amount :',discount_rate)
    print('To Pay Amount :',final_amount)

  elif user_input == 8:
    print('Thank you using our PERSONAL FINANCE CALCULATOR')
    break
  else:
    print('Invalid! Try Again')
    