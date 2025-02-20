# Zoe jimenez, UPDATE Financial calculator PYTHON
def info(cost, income, type):
    percent = (cost/income)*100
    print(f"Your {type} is {cost:.2f} Which is {percent}% of your income.\n" )

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
transportation = float(input("What is your transportation cost?\n"))
saving = income*.1
savings = (saving/income)*100
spending = income-saving-rent-groceries-utilities-transportation
spendings = (spending/income)*100


info(rent, income, "rent")
info(utilities, income, "utlities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")