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


#Function to get the random word and change to uppercase
def random_word():
        word = random.choice(word_list)
        return word.upper()