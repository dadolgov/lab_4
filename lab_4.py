"""
Card Dealer
Author: Dmitrii Dolgov
Deals a user-specified ammount of random cards
Date:2/8/2026
"""

import random
# initializing deck 
card_suits=["c", "h", "s", "d"]
card_values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck=[]
hand=[]

# filling the deck list
for suit in card_suits:
    for value in card_values:
        deck.append(suit + value)

# drawing cards
number_of_cards=int(input("Write the number of cards: "))
# Protection from drawing too many cards
while number_of_cards > 52 or number_of_cards < 0:
    print("Wrong number of cards! Draw between 0 and 52!")
    number_of_cards = int(input("Write the number of cards: "))
# filling the player's hand with random cards
for _ in range(number_of_cards):
    current_card = random.randint(0,len(deck) - 1)
    hand.append(deck.pop(current_card))

# Results output
print("Your cards are:")
print(*hand, sep=", ")
print("Total cards in hand: ", len(hand))