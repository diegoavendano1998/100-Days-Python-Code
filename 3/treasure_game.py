print("""
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|                  _|___|___|___|___|___|___|
___|___|___|___|___|___|__  Treasure Game   ___|___|___|___|___|___|__
_|___|___|___|___|___|___|                  _|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|__
_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
""")
choice1 = input("You're on a crossroad, where do you want to go? [left/right]").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake do you swim o wait for a boat? [swim/wait]").lower()
    if choice2 == "wait":
        choice3 = input("Now you find a house with three doors, what door do you choose? [1/2/3]")
        if choice3 == "1":
            print("The door have a an alligator inside. Game Over :(")
        if choice3 == "2":
            print("You didn't find the treasure :( but you're still alive!")
        if choice3 == "3":
            print("Congratulations, you find the treasure!!!")
    else:
        print("Now you are the dinner of a really big shark :(")
else:
    print("Game Over :(")

