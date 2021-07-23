income = float(input("Enter the annual income: "))

if income  <= 85528:
    tax = ((income *.18) -556.02) 
# Write your code here.

else income > 85528:
tax = ((income -14839.02) + .32*tax)

tax = round(tax, 0)
print("The tax is:", tax, "thalers")