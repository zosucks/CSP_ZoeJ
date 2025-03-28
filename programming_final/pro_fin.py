#PROGRAMMING FINAL PYTHON
#featuring Brahm, Gov, Kaleb, and Zoe
import random
print("Welcome to hangman, begin if you DAREEEE!!")


#kaleb: function that runs when the user fails or wins then repeats the code
def play_hangman(word):
    #Sets how many attempts user has
    attempts = 6  

    #Opens a variable for the going to be guessed letters
    guessed_letters = []

    #Then this opens the visual part of the hangman
    hangman_pictures = [
        """
         _______
         |   |
         |
         |
         |
         |
        [][][]]""",
        """
         _______
         |   |
         |   O
         |
         |
         |
        [][][]]""",
        """
         _______
         |   |
         |   O
         |   |
         |
         |
        [][][]]""",
        """
         _______
         |   |
         |   O
         |  /|
         |
         |
        [][][]]""",
        """
         _______
         |   |
         |   O
         |  /|\\
         |
         |
        [][][]]""",
        """
         _______
         |   |
         |   O
         |  /|\\
         |  /
         |
        [][][]]""",
        """
         _______
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        [][][]]"""
    ]

#Brahm: loop that makes the whole game work as it inserts the guessed letter or not
    while attempts > 0:
        print(hangman_pictures[6 - attempts])
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"Word: {display_word}")



#Zoe: a conditional that plays when the player the user finishes the word
        if display_word == word:
            print("Congratulations! You guessed the word!")
            play_again()

#Kaleb:  a variable for user's guess
        guess = input("Guess a letter: ").lower()

#Zoe: Conditional check for a valid guess
        if guess in guessed_letters:
            print("You already guessed that letter? Please try again...")
        elif guess in word:
            print(f"Goodjob! '{guess}' is in this word.")
            guessed_letters.append(guess)
        else:
            print(f"Nope! '{guess}' is not in this word.")
            guessed_letters.append(guess)
            attempts -= 1  

#Gov: Plays when user runs out of guesses
    print(hangman_pictures[-1])
    print(f"Game over! The word was '{word}', better luck next time!")
    play_again()

#Zoe: Calls whole code again if user wants to play again, A function with a conditional
def play_again():
    again = input("Would you like to play again? (Y/N)").upper()
    if again == "Y":
        the_words()
    elif again == "N":
        exit()
    else:
        print("That isn't a Y or an N! Try again! :(")
        play_again()

#Gov: the function that chooses the random word in a list
def the_words():
    words = ["software", "iconic", "dirtbike", "manager", "pepsi", "explode", "investigator", "exciting", "attitude", "computer", "cyber", "architect", "printer", "gatos", "publication", "evaluation", "rhinoceros", "pharoah", "crocodile", "alligator", "pneumonoultramicroscopicsilicovolcanoconiosis", "supercalifragilisticexpialidocious", "lebron"]
    random_words = random.choice(words)
    play_hangman(random_words)

the_words()