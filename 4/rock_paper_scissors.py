import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

images = rock,paper,scissors
user_choice = int(input("What do you choose? [0-rock/1-paper/2-scissors]\n"))
computer_choice = random.randint(0,2)
if user_choice > 2 or user_choice < 0:
    print("Invalid value")
else:
    print(images[user_choice])
    print(f"Computer choice {computer_choice}")
    print(images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("Computer wins!")
    elif computer_choice > user_choice:
        print("Computer wins!")
    elif computer_choice < user_choice:
        print("You wins!")
    elif computer_choice == user_choice:
        print("Its a Draw!")



