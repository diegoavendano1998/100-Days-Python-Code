# Hangman Game
from hangman_words import word_list
import random


print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')

# word_list = ["hola","diego","navidad"]
chosen_word = random.choice(word_list)
display = ["_" for _ in range(len(chosen_word))]
print(display)
print(chosen_word)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
game_over = False
lives = 6
letters_guess = []

while(not game_over):
    guess = input("Letter:\t").lower()
    if guess not in letters_guess:
        letters_guess += guess
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = guess
        if guess not in chosen_word:
            print(f"The letter {guess} is not in the word")
            lives -= 1
            if lives == 0:
                game_over=True
                print("You lose")
        if not "_" in display:
            game_over=True
            print("You win!")
    else:
        print(f"You have already input the letter {guess}!")
    print(stages[lives])
    print(" ".join(display))








