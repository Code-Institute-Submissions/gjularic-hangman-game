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
while wrong_guess < max_guess and current_guess != word:
        print(HANGMAN[wrong_guess])
        print("Letters that have been used: ", guessed_letters)
        print("Your guess so far: ", current_guess)
        user_guess = input("Type in the letter and see if it's in the word: ").upper() # get user input letter and change to uppercase
        guessed_letters.append(user_guess) # add the letter to the list of used letters

        

        
