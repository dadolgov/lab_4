"""
Card Dealer
Author: Dmitrii Dolgov
Deals a user-specified ammount of random cards
Date:2/8/2026
"""

import random

card_suits=["c", "h", "s", "d"]
card_values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck=[]

for suit in card_suits:
    for value in card_values:
        deck.append(suit+value)
print(deck)

    