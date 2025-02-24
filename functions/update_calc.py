# Zoe jimenez, UPDATE Financial calculator PYTHON

print("Welcome User! This is a financial Calculator for your needs.")
def user_inputs(type):
    
    float(input(f"What is your {type}?: "))
 
income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
groceries = user_inputs("groceries")
transportation = user_inputs("transportion")



# print statment that welcomes user and tells what this program does
#print("Welcome User! This is a financial Calculator for your needs.")
# ask what their monthly income is (variable an input)
#income = float(input("What is your income?: \n"))
# ask what their rent is (variable an input)
#rent = float(input("What is your rent?\n"))
# ask what their utilities cost is (variable an input)
#utilities = float(input("What is your utilities cost?\n"))
# ask what their  grocories cost is (variable an input)
#groceries = float(input("What is your groceries cost?\n"))
# ask what their transportation cost is (variable an input)
#transportation = float(input("What is your transportation cost?\n"))

def info(cost, type):
    percent = (cost/income)*100
    print(f"Your {type} is {cost:.2f} Which is {percent}% of your income.\n" )




saving = income*.1
savings = (saving/income)*100
spending = income-saving-rent-groceries-utilities-transportation
spendings = (spending/income)*100


info(rent, "rent")
info(utilities, "utlities")
info(groceries, "groceries")
info(transportation, "transportation")
info(savings, "savings")
info(spending, "spending")

