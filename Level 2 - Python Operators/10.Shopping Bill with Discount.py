amount = float(input('Enter your amount :'))

if amount < 1000 :
    discount = 0
elif amount < 5000:
    discount = 10
elif amount < 10000:
    discount = 20
elif amount < 20000:
    discount = 30
else:
    discount = 40

discount_rate = amount * discount / 100
final_amount = amount - discount_rate

print('\nOriginal Amount',amount)
print('Dicount Amount :',discount_rate)
print('To Pay Amount :',final_amount)


    
    
    
