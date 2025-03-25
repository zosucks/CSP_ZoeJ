#PROGRAMMING FINAL PYTHON
print("Welcome to hangman!")
print("______________")
print("|            |")
print("|             ")
print("|             ")
print("|             ")
print("[][][]        ")


#Brahm: loop/ which word(in a list) to make the user guess
import random
random_words = random.choice["software", "iconic", "dirtbikes", "manager", "pepsi", "explode", "investagator", "exciting", "attitude", "computer", "cyber", "architect", "printer", "publication", "evaluation", "rhinoceros", "pharoah", "crocodile", "alligator", "pneumonoultramicroscopicsilicovolcanoconiosis"]

for word in words:
   print (random.random(word))


#Kaleb: function that runs if they get the letter wrong (includes making the hangman if wrong)
def wrd(wrong):
    float(input(f"What is your {wrong}?\n"))


#Gov: the other function that runs when the user gets it correct (includes spelling the word at the bottom)
def letter(right):
    (input(f"What is your {right}?\n"))



#Zoe: conditional runs when the user fails or wins then repeats the code
