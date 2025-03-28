# Zoe jimenez, UPDATE Financial calculator PYTHON

print("Welcome User! This is a financial Calculator for your needs.")
def user_inputs(type):
    float(input(f"What is your {type}?: "))
    return float


income = user_inputs("income")
rent = user_inputs("rent")
utilities = user_inputs("utilities")
groceries = user_inputs("groceries")
transportation = user_inputs("transportion")

saving = float(income*.1)
savings = float((saving/income)*100)
spending = float(income-saving-rent-groceries-utilities-transportation)
spendings = float((spending/income)*100)


def info(cost, income, type):
    percent = (cost/income)*100
    print(f"Your {type} is {cost:.2f} Which is {percent}% of your income.\n" )
    return
    



info(rent, income, "rent")
info(utilities, income, "utlities")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")
info(spending, income, "spending")





