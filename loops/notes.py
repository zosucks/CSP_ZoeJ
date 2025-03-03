#Zoe Jimenez, Loops notes PYTHON

#What is a loop? 


#What are the two types of loops?
#for loop
nums = [12,3,66,7,3,3,2]

for num in nums:
    print(num)


    #while loops

x = 0
while x < 10:
    print(x)
    x+= 1

#What is iteration
#That specific instance of the loop
#Iteration the amount of times you are looping through


#What are lists? 
num = [1,2,3,4,5,6,7,6]
siblings = ["Alex", "Katie", "Anderw", "Tia"]
print(nums) #prints whole ugly list
print(siblings[3])

siblings[3] = "jake"
print(siblings[3])

siblings.pop(2)
siblings.insert(1, "Jayshree")
siblings.insert(2, ["Joe", "Noah", "Zee"])
print(siblings)

#How do you make lists in python? 
#Use straight braketts, add items with correct data types(strings have quotation makes and interigers have none), they have to have commas between them

#How do you make for loops in python? 
for sibling in siblings:
    print(sibling)

for x in range(1,6,3):
    print(x)

#How do you make while loops in python?
import random
x = 1 #variable to keep count of iteration
goose = random.randint(1,20)

while x <= 20:
    if x == goose:
        print("GOOSE")
        break #stops when goose appears
    else:
        print("Duck..")
    x+= 1

#How do you make lists in C?


#how do you make for loops in C?


#How do you make while loops in C?
