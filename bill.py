units=int(input("What is the number of units consumed?"))

if units<50:
    amount=units*2.6
    tax=25
elif units<=100:
    amount=(units*2.6)+((units-50)*3.25)
    tax=35
elif units<=200:
    amount=(units*2.6)+((units-50)*3.25)+((units-100)*5.26)
    tax=45
else:
    amount=(units*2.6)+((units-50)*3.25)+((units-100)*5.26)+((units-200)*8.45)
    tax=75
    
total_amount=amount+tax
print("Electricity bill is", total_amount)