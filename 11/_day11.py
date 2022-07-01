# Blackjack project

from art import logo
import random

def deal_card():
    """Return random card from the deck"""
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    """Return the sum of a list of cards"""
    total_score = sum(cards)
    if total_score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total_score > 21:
        cards.remove(11)
        cards.append(1)
        calculate_score(cards)
    return total_score

def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, computer has a BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "Lose, You went over 21"
    elif computer_score > 21:
        return "Win, Computer went over 21"
    elif user_score > computer_score:
        return "Win, your score is greather than computer"
    else:
        return "Lose, your score is lower than computer"



def play_blackjack():
    print(logo)
    print("\n")
    
    user_cards = []
    computer_cards = []

    # Fill the two initial cards for user and computer
    for _ in range(2):
        # user_cards.extend(new_card) -> Cooncatena una lista a otra
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\tYour cards: {user_cards}, current score {user_score}")
        print(f"\tComputer's first card {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to get another card [y/n]: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer should keep getting cards until score < 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n"*2)
    print("*"*60)
    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Computer cards: {computer_cards}, computer score {computer_score}\n")
    print(compare_scores(user_score,computer_score))

while input("\nDo you want to play BlackJack? [y/n]: ").lower() == "y":
    print("\n"*5)
    play_blackjack()