class Card:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.hard,self.soft=self._points()
class NumberCard(Card):
    def _points(self):
        return int(self.rank),int(self.rank)
class AceCard(Card):
    def _points(self):
        return 1,10
class FaceCard(Card):
    def _points(self):
        return 10,10

class Suit:
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol
cards=[AceCard("2","*"),NumberCard("A","*"),FaceCard("3","#")]
print(cards)