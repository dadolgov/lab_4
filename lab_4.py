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

# filling the deck list
for suit in card_suits:
    for value in card_values:
        deck.append(suit+value)
print(deck)

# drawing random cards from deck
number_of_cards=int(input("Write the number of cards: "))

for _ in range(number_of_cards):
    print(deck.pop(random.randint(0,len(deck)-1)))

print(deck)