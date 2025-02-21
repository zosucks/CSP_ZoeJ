# Zoe jimenez, function notes PYTHON

#functions hold actions to be reused
#number = int(input("Please tell me a number: \n"))
#def add(numOne, numTwo):
    #numOne = int(input("Please tell me a number: \n"))
    #numTwo = int(input("Please tell me another number: \n"))

 #   return numOne + numTwo
    #print(numOne+numTwo)


#add(number,267)
#print(add(8,354))
#addition = add(34,657)
#add(addition,965)
#add(3,284)

def values(type):
    return input(f"Please give me a {type}:")

name = values ("name")
place = values ("place")
verb = values ("verb (past tense)")

print(f"{name} was really fast getting to {place} by {verb} the whole way there.")