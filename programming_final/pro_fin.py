#PROGRAMMING FINAL PYTHON
#featuring Brahm, Gov, Kaleb, and Zoe
import random
print("Welcome to hangman!")


#kaleb: function that runs when the user fails or wins then repeats the code
def play_hangman(word):
    #Sets how many attempts user has
    attempts = 6  
    #Opens a variable for the going to be guessed letters
    guessed_letters = []
    #Then this opens the visual part of the hangman
    hangman_pictures = [
        """
         -----
         |   |
         |
         |
         |
         |
        [][][]]""",
        """
         -----
         |   |
         |   O
         |
         |
         |
        [][][]]""",
        """
         -----
         |   |
         |   O
         |   |
         |
         |
        [][][]]""",
        """
         -----
         |   |
         |   O
         |  /|
         |
         |
        [][][]]""",
        """
         -----
         |   |
         |   O
         |  /|\\
         |
         |
        [][][]]""",
        """
         -----
         |   |
         |   O
         |  /|\\
         |  /
         |
        [][][]]""",
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        [][][]]"""
    ]

#Brahm: loop/ which word(in the list) to make the user guess
    while attempts > 0:
        print(hangman_pictures[6 - attempts])
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(f"Word: {display_word}")



# a condtional that plays when the player the user finishes the word
        if display_word == word:
            print("Congratulations! You guessed the word!")
            return

# Makes a variable for user's guesses
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


    print(hangman_pictures[-1])
    print(f"Game over! The word was '{word}'.")

# #Gov: the function that chooses the random word in a list
def the_words():
    words = ["software", "iconic", "dirtbike", "manager", "pepsi", "explode", "investigator", "exciting", "attitude", "computer", "cyber", "architect", "printer", "gatos", "publication", "evaluation", "rhinoceros", "pharoah", "crocodile", "alligator", "pneumonoultramicroscopicsilicovolcanoconiosis", "supercalifragilisticexpialidocious", "lebron"]
    random_words = random.choice(words)
    play_hangman(random_words)

the_words()