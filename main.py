import random


# Function that uses List *cards* to *return* a random card.
# 11 is the Ace, 10 is Jack, Queen, King and the other cards 1 - 9.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Deal the user and computer 2 cards each
user_cards = []
computer_cards = []
for _ in range(2):    
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(user_cards, computer_cards)

# Function calculate_score() that takes a List of cards as input 
# and returns the score.
def calculate_score(cards):
    # 0 will represent a blackjack in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # 11 is Ace. If the score is over 21 Ace becomes 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)
print(calculate_score(user_cards))

