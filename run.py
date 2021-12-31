#Importing "random" to get the random word and word list
import random
from wordList import word_list

#Hangman display
HANGMAN = [
"""        -------
        |     |
        |      
        |        
        |      
        |        
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |        
        |      
        |        
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |     |  
        |      
        |        
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |    /|  
        |      
        |        
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |    /|\ 
        |      
        |        
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |    /|\ 
        |     |
        |        
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |    /|\ 
        |     |
        |    /   
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/""","""
        -------
        |     |
        |     O
        |    /|\ 
        |     |
        |    / \\
   _____|__________
  /     |         /|
 /_______________/ |
|                | /
|________________|/"""
]

#Main game
def first_display():
        print("""
{}    {}    {}{}     {}    {}    {}}}}}    {}      {}    {}{}     {}    {}
{}    {}   {}  {}    {}}}  {}   {}    {}   {}}}  {{{}   {}  {}    {}}}  {}
{}{{}}{}  {}{{}}{}   {} {} {}   {}         {} {{}} {}  {}{{}}{}   {} {} {}
{}    {}  {}    {}   {}  {{{}   {}  {{{{   {}  {}  {}  {}    {}   {}  {{{}
{}    {}  {}    {}   {}    {}    {}}}}}    {}      {}  {}    {}   {}    {}
        """)
        print(HANGMAN[7])
        name = input("Enter your name: \n")
        print("Welcome", name, "!")
        print("Try to guess the word before the stickman gets hanged, you have 7 guesses available!")

def start_game():
        #Main Variables
        global word
        global current_guess
        global max_guess
        global wrong_guess
        global guessed_letters
        word = random.choice(word_list).upper()
        current_guess = "-" * len(word)
        max_guess = 7
        wrong_guess = 0
        guessed_letters = []
        # Main loop that checks if user has enough guesses left to continue,
        # to end the game if the whole word was guessed,
        # or if user failed to guess it and ran out of guesses
        while wrong_guess < 7 and current_guess != word:
                print(HANGMAN[wrong_guess])
                print("Letters that have been used: ", guessed_letters)
                print("Your guess so far: ", current_guess)
                user_guess = input("Type in the letter and see if it's in the word: \n").upper() # get user input letter and change to uppercase
                
                # while statement to check if the user typed in the number, which is not allowed
                while user_guess.isdigit() or len(user_guess) != 1:
                        user_guess = input("Numbers and multiple letters are not allowed! Type in 1 letter: \n").upper()

                # while statement to check if the letter was already guessed
                while user_guess in guessed_letters:
                        print("You have already tried the letter:", user_guess)
                        user_guess = input("Type in another letter: \n").upper()

                guessed_letters.append(user_guess) # add the letter to the list of used letters

                # Check if the user guess is correct
                # and get the current status of the word
                # with letters and dashes included
                if user_guess in word:
                        print("Correct! Letter", user_guess, "is in the word.")

                        # Update the status of the word
                        update_current_guess = ''
                        for i in range(len(word)):
                                if user_guess == word[i]:
                                        update_current_guess += user_guess
                                else:
                                        update_current_guess += current_guess[i]

                        current_guess = update_current_guess

                else:
                        print("Wrong :( Letter", user_guess, "is not in the word.")
                        wrong_guess += 1  # Incrementing wrong guess so that the hangman status can be displayed correctly
                        max_guess -= 1    # Decrementing maximum amount of guesses so that game can end if failed

                print("Chances left:", max_guess)


#Ending the game
def end_game():
        if wrong_guess == 7:
                print(HANGMAN[wrong_guess])
                print("Stickman has been hanged! You Lost!")  
                print("Correct word is:", word)
        else:
                print("You saved the Stickman! You Won!")

# Play again function
def play_again():
        user_response = input("Do you want to play again? Y/N: \n").upper()
        if user_response == "Y":
                return hangman()
        else:
                print("Thanks for playing!")


def hangman():
        start_game()
        end_game()
        play_again()

first_display()
hangman()


        

        
