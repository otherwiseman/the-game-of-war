"""
Simulate the card game War. A reminder of the basic rules:
1. Each player gets 26 cards. The deck of [52] gets split equally.
2. Each player flips one of their cards, higher card wins, winner takes both.
3. If 2 cards played are of equal value, then a war ensues.Both players place
   the next 3 cards of their pile face down, and then another card face-up.
   Winner is the owner of the higher value face-up card. If face-up cards are
   equal, another war ensues until one player has a card higher then their
   opponent. Winner takes all cards.
4. War is over when one player runs out of cards. Player with cards remaining is
   victorious.

"""

import random

def create_deck(suits=4, card_types=13):
    "Create a random shuffled deck of cards."
    cards = []
    for suit in range(suits):
        for card_type in range(1, card_types+1):
            cards.append(card_type)
    random.shuffle(cards)
    return cards

def its_war(deck):
    x_cards = deck[:len(deck)/2]
    y_cards = deck[len(deck)/2:]
    x_stash = []
    y_stash = []


    round = 1
    while x_cards and y_cards:
        # use pop to play from end forward
        x_card = x_cards.pop()
        y_card = y_cards.pop()

        if x_card == y_card:
            x_stash.extend([x_card]+x_cards[-3:])
            x_cards = x_cards[:-3]
            x_cards.append(x_stash.pop())

            y_stash.extend([y_card]+y_cards[-3:])
            y_cards = y_cards[:-3]
            y_cards.append(y_stash.pop())
        elif x_card > y_card:
            x_cards = [x_card, y_card] + x_stash + y_stash + x_cards
            x_stash = []
            y_stash = []
        elif y_card > x_card:
            y_cards = [y_card, x_card] + y_stash + x_stash + y_cards
            x_stash = []
            y_stash = []

        print "round %s: x_cards: %s, x_stash %s, y_cards %s, y_stash %s" % (round, len(x_cards), len(x_stash), len(y_cards), len(y_stash))
        round += 1

if __name__ == "__main__":
    deck = create_deck()
    its_war(deck)
    
                                                                    
                           
