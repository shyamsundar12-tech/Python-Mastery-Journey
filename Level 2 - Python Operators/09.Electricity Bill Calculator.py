units = float(input('Enter your units :'))

if units <= 100:
    bills = units * 5
elif units <=200:
    bills = (100 * 5) + ((units - 100) * 7)
elif units <=300:
    bills = (100 * 5) + (100 * 7) + ((units - 200) * 10)
else:
    bills = (100 * 5) + (100 * 7) + (100 * 10 ) + ((units - 300) * 15)

print('Total Amount :',bills)  


