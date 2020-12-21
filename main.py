import random
from replit import clear


# Function that uses List *cards* to *return* a random card.
# 11 is the Ace, 10 is Jack, Queen, King and the other cards 1 - 9.
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    print(card)
    return card


# Function calculate_score() that takes a List of cards as input 
# and returns the score.
def calculate_score(cards):
    # 0 will represent a blackjack in the game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # 11 is Ace. If the score is over 21 Ace becomes 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)
#print(calculate_score(user_cards), calculate_score(computer_cards))


def play_game():
    is_game_over = False
    #Deal the user and computer 2 cards each
    user_cards = []
    computer_cards = []
    for _ in range(2):    
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(user_cards, computer_cards)
    print(calculate_score(user_cards), calculate_score(computer_cards))
    while not is_game_over:
        # Show user's cards and the computer's first card and show the user's score.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        #If the game has not ended, ask the user if they want to draw another card or the game.
        if user_score == 0 or computer_score == 0 or user_score > 21:            
            is_game_over = True
            print("THE END")
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
        # Once the user is done, it's time to let the computer play. 
        # The computer should keep drawing cards as long as it has a score less than 17.
        while computer_score !=0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    
        

# Clear the console and start the game
while input("Do you want play a game of Black Jack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
