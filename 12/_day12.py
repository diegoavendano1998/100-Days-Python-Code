"""
Scope
Es el alcance que tiene un elemento dentro del proyecto.

Local Scope
Los elementos que existen solo dentro de los metodos
    def some_method():
        var = 1000
        print(var) -> 1000
    
    print(var) -> var is not defined

Global Scope
Los elementos que existen dentro y fuera de los metodos.
    var = 1000

    def some_method():
        print(var) -> 1000
    
    print(var) -> 1000

Para modificar una variable global es necesario utilizar la palabra resrvada 'global':
    var = 1000

    def some_method():
        global var
        var = 2000
    
    print(var) -> 2000

Global Scope es muy utilizado para declarar constantes que se ocuparan dentro del codigo
    PI = 3.14159

    def print_pi()
        print(PI)
"""

from art import logo
import random

LEVELS = ["easy","hard"]

def set_attempts():
    while True:
        difficulty = input("Choose the difficulty [easy/hard]:\t")
        if difficulty.lower() in LEVELS:
            attempts = 10 if difficulty == "easy" else 5
            return attempts
        else:
            print("Invalid difficulty")

def play_guess_number():
    random_number = random.randint(1,100)
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    attempts = set_attempts()
    is_game_over  = False

    while not is_game_over:
        if attempts > 0:
            print(f"You have {attempts} remaining to guess the number")
            guess = int(input("Make a guess:\t"))
            if guess == random_number:
                print("Congratulations, you find the correct number!")
                is_game_over = True
            else:
                if guess < random_number:
                    print("Too low")
                else:
                    print("Too high")
                attempts -= 1
        else:
            print(f"No attempts remaining :(, the number was {random_number}")
            is_game_over = True

while input("\n\nPress Y to play:\t").lower() == "y":
    play_guess_number()

