# Zoe Jimenez, conditionals notes PYTHON
name = input("What is your name?: \n")
#What puts something inside of the “if” statement?
if name == "LaRose":
    print("Hi mrs. Larose")
else: #this happens if the condition is false
    print(f"Hello {name}!")


#What do if statements do?
#Checks a condition and if it is true then it will do a thing
if name == "LaRose": #<= this is a condition
    print("Hi mrs. Larose")


#What are boolean statements? 
#A part of the conditional that is true or false or a true or false statement
#if name == "LaRose": <= a boolean statement

#What do else statements do?
#if the boolean is false then the else statement happens


#What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cookies are there?: \n"))
#computers read top to bottom, check the least likely first.
if num == 0: #<= if always starts the conidtional
    print("There are none.")
elif num == 1:
    print("There is one")
elif num <4:
    print("Theres a couple.")
elif num < 10:
    print("There are a few.")
else: #<= else always ends the conditionals
    print("There are many.")

#What do each of the different symbols mean in conditionals?
#< - less then
#> - greater than
#<= - less than or equal to
#>= - greater than or equal to
#== - equal to
#=== - (NOT IN PYTHON) check if the data type is the same
#! - not

#What are the 3 logical operators?
if num <10 and num > 5: #And means both booleans are true
    print("This is a single digit number")

elif num <10 or num > 5: #Or means one booleans must true
    print("This is a big single digit number")

elif not num <10: #Not changes to check if false
    print("This is a not single digit number")
#What are logical operators for?
#allows the code to handle mote difficult questions, increases complexity


#What does a nested conditional statement do?
if num <10:
    if num == 8:
        print("This prints at 8")
elif:
    print("The number is less than 10")
else:
    print("The number is bigger then 10")

#How do you write an if statement in C?


#How do you write else statements in C?


#How do you write elif/ else if statements in C?


#How do you write the 3 logical operators in C?

