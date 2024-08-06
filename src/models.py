class Desk:
    cards : dict[str, int] = {} 
    def __init__(self, cards):
        self.cards = cards
    
    def addCards(self, cards) -> None:
        for card in cards:
            if card in self.cards:
                self.cards[card] += 1
            else:
                self.cards[card] = 1

class Deck:
    cards : dict[str, int] = {} 
    def __init__(self, cards):
        self.cards = cards
    
    def getSolution(self, cards) -> None | list[str]:
        # much of the code here
        return None
    
    def addCard(self, cards) -> None:
        for card in cards:
            if card in self.cards:
                self.cards[card] += 1
            else:
                self.cards[card] = 1
    
    def removeCard(self, cards) -> None:
        for card in cards:
            if card in self.cards:
                self.cards[card] -= 1
                if self.cards[card] == 0:
                    del self.cards[card]
            else:
                print(f"Card \"{card}\" not found in deck")