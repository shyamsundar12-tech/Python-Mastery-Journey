cost_price = float(input('Enter your cost price :'))
selling_price = float(input('Enter your selling price :'))
if cost_price < selling_price:
    Profit = selling_price - cost_price
    print('Profit')
    print('Profit Amount = ',Profit)
else :
    loss = cost_price - selling_price    
    print('Loss')
    print('Loss Amount = ',loss)