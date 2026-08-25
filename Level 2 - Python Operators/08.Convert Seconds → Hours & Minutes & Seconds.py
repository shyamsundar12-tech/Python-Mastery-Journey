total_second = int(input('Enter the Total Seconds : '))

hour = total_second//3600
remaining_seconds = total_second % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds%60

print('Seconds :',seconds,'SEC')
print('Minutes :',minutes,'MIN')
print('Hours :',hour,'HR')
total = hour + minutes+seconds
print(f'{total} Hours {minutes} Min {seconds} SEC')