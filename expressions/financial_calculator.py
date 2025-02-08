# Zoe jimenez, Financial calculator PYTHON

# print statment that welcomes user and tells what this program does
print("Welcome User! This is a financial Calculator for your needs.")
# ask what their monthly income is (variable an input)
income = float(input("What is your income?: \n"))
# ask what their rent is (variable an input)
rent = float(input("What is your rent?\n"))
# ask what their utilities cost is (variable an input)
utilities = float(input("What is your utilities cost?\n"))
# ask what their  grocories cost is (variable an input)
groceries = float(input("What is your groceries cost?\n"))
# ask what their transportation cost is (variable an input)
transportation = float(input("What is your transportation?\n"))

savings = income - rent - groceries - utilities - transportation
# calculate spending as [income - savings - rent - groceries - utilities - transportation] (variable)
#spending = income - savings - rent - groceries - utilities - transportation
# calculate savings as 10% of income (income * .1) (a variable)
saving = income*.1
# calculate percent income of rent (rent/income * 100) (variable)
rents = (rent/income)*100 
# calculate percent income of utilities (utilities/income * 100) (variable)
utilitie = (utilities/income)*100
# calculate percent income of groceries (groceries/income * 100) (variable)
grocerie = (groceries/income)*100 
# calculate percent income of transportation (transportation/income * 100) (variable)
transportations = (transportation/income)*100 
# calculate spending as [income - savings - rent - groceries - utilities - transportation] (variable)
spending = income-savings-rent-groceries-utilities-transportation
# calculate percent income of spending (spending/income * 100) (variable) {NOT NESSARY}
spendings = (spending/income)*100

# your rent is $XX.XX which is XX% of your income. (print)
print("Your rent is $", rent, "Which is", rents, "% of your income.\n" )
# your utilites is $XX.XX which is XX% of your income. (print)
print("Your utilities is $", utilities, ", Which is", utilitie, "% of your income.\n")
# your groceries is $XX.XX which is XX% of your income. (print)
print("Your groceries is", groceries, ",Which is", grocerie, "% of your income.\n")
# your transportation is $XX.XX which is XX% of your income. (print)
print("Your transportation is",transportation, "Which is", transportations, "% of your income \n")
# your savings is $XX.XX which is XX% of your income. (print)
print("Your savings is $", savings, ", Which is", saving, "% of your income.\n")
# your spending is $XX.XX which is XX% of your income. (print)
print("Your spending is $", spending, ", Which is", spendings, "% of your income\n")