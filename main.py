#!/usr/bin/env python3
from src.models import *
from src.utils import *
from src.menu import *

TYPES = ['cuori', 'denari', 'fiori', 'picche']
VALUES = [
    'asso','due', 'tre', 'quattro', 'cinque',
    'sei', 'sette', 'otto', 'nove', 'dieci',
    'jack', 'regina', 're'
]

def main():
    desk = Desk({})
    deck = Deck(askCards(TYPES, VALUES))
    while True:
        choice = printMenu()
        if choice == '1':
            deck.addCard(askCard(TYPES, VALUES))
        elif choice == '2':
            print(deck.getSolution(desk.cards))
        elif choice == '3':
            desk.addCards(askCards(TYPES, VALUES))
        elif choice == '4':
            break
        else:
            print("Invalid choice")
    
if __name__ == "__main__":
    main()