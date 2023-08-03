import card as c
import random as r
import math as m

class Deck:
  def __init__(self):
    self.deck = []

    # prepares full deck of cards
    for i in range(1, 14):
      for j in range(4):
        self.deck.append(c.Card(i, j))

  def RandomCard(self):
    return m.floor(r.random() * 52)

  def Shuffle(self):
    for i in range(3):
      for j in range(52):
        randNum = self.RandomCard()

        # shuffles internally by swapping card with card at random index
        if randNum != j:
          temp = self.deck[j]
          self.deck[j] = self.deck[randNum]
          self.deck[randNum] = temp

    randNum = self.RandomCard()

    # cuts deck at random location (adds cards at beginning to end)
    for i in range(randNum):
      self.deck.append(self.deck.pop(0))

  def __getitem__(self, key):
    return self.deck[key]

  def PrintDeck(self):
    for card in self.deck:
      print(str(card))