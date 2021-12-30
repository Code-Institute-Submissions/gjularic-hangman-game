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

print("Hangman game")
print(HANGMAN[7])
name = input("Enter your name: ")
print("Welcome", name, "!")
print("Try to guess the word before the stickman gets hanged, you have 7 guesses available!")


#Main Variables
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
        user_guess = input("Type in the letter and see if it's in the word: ").upper() # get user input letter and change to uppercase
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
if wrong_guess == 7:
        print(HANGMAN[wrong_guess])
        print("Stickman has been hanged! You Lost!")  
        print("Correct word is:", word)
else:
        print("You saved the Stickman! You Won!") 


        

        
