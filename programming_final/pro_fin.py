#PROGRAMMING FINAL PYTHON
#featuring Brahm, Gov, Kaleb, and Zoe
import random



#kaleb: conditional runs when the user fails or wins then repeats the code
print("Welcome to hangman!")

def play_hangman(word):
   
    attempts = 6  
    guessed_letters = set()
    hangman_states = [
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

   #Brahm: loop/ which word(in a list) to make the user guess
    while attempts > 0:
        print(hangman_states[6 - attempts])
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"Word: {display_word}")

        # Check if the player has guessed the word
        if display_word == word:
            print("Congratulations! You guessed the word!")
            return

        # Ask for a guess
        guess = input("Guess a letter: ").lower()

        #Zoe: Conditional check for valid guess
        if guess in guessed_letters:
            print("You already guessed that letter? Please try again...")
        elif guess in word:
            print(f"Goodjob! '{guess}' is in this word.")
            guessed_letters.add(guess)
        else:
            print(f"Nope! '{guess}' is not in this word.")
            guessed_letters.add(guess)
            attempts -= 1  


    print(hangman_states[-1])
    print(f"Game over! The word was '{word}'.")

# #Gov: the function that chooses the random word in a list
if __name__ == "__main__":
    words = ["software", "iconic", "dirtbike", "manager", "pepsi", "explode", "investiagator", "exciting", "attitude", "computer", "cyber", "architect", "printer", "publication", "evaluation", "rhinoceros", "pharoah", "crocodile", "alligator", "pneumonoultramicroscopicsilicovolcanoconiosis", "lebron"]
    random_words = random.choice(words)
    play_hangman(random_words)