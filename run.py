#Importing "random" to get the random word and word list
import random
from wordList import word_list

#Main varibles
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
