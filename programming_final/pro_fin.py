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
words = ["software", "iconic", "dirtbike", "manager", "pepsi", "explode", "investiagator", "exciting8", "attitude", "computer", "cyber", "architect", "printer", "publication", "evaluation", "rhinoceros", "pharoah", "crocodile", "alligator", "pneumonoultramicroscopicsilicovolcanoconiosis", "bombaclat"]
random_words = random.choice(words)
for random_word in words:
    if random_word == "software" or "dirtbike" or "exciting" or "attitude" or "computer" :
        print("_ _ _ _ _ _ _ _")
    elif random_word ==  "manager" or "explode" or "pharoah" or "printer":
        print("_ _ _ _ _ _")
    elif random_word == "iconic":
        print("_ _ _ _ _ _ _")
    elif random_word == "pepsi" or "cyber":
        print("_ _ _ _ _")
    elif random_word ==  "crocodile" or "alligator" or "architect" or "bombaclat":
        print("_ _ _ _ _ _ _ _ _")
    elif random_word == "evaluation" or "rhinocero":
        print("_ _ _ _ _ _ _ _ _ _")
    elif random_word == "publication":
        print("_ _ _ _ _ _ _ _ _ _ _")
    else:
       print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")


if random_word == "software" or "dirtbike" or "exciting" or "attitude" or "computer" :
        print("_ _ _ _ _ _ _ _")
    elif random_word ==  "manager" or "explode" or "pharoah" or "printer":
        print("_ _ _ _ _ _")
    elif random_word == "iconic":
        print("_ _ _ _ _ _ _")
    elif random_word == "pepsi" or "cyber":
        print("_ _ _ _ _")
    elif random_word ==  "crocodile" or "alligator" or "architect" or "bombaclat":
        print("_ _ _ _ _ _ _ _ _")
    elif random_word == "evaluation" or "rhinocero":
        print("_ _ _ _ _ _ _ _ _ _")
    elif random_word == "publication":
        print("_ _ _ _ _ _ _ _ _ _ _")
    else:
       print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")



#for word in word:
#   print (random.random(word))


#Kaleb: function that runs if they get the letter wrong (includes making the hangman if wrong)
def wrd(wrong):
    float(input(f"What is your {wrong}?\n"))


#Gov: the other function that runs when the user gets it correct (includes spelling the word at the bottom)
def letter(right):
    (input(f"What is your {right}?\n"))



#Zoe: conditional runs when the user fails or wins then repeats the code
