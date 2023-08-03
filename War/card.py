class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit

  def __str__(self):
    if self.value >= 2 and self.value <= 10:
      temp = str(self.value)
    elif self.value == 1:
      temp = 'A'
    elif self.value == 11:
      temp = 'J'
    elif self.value == 12:
      temp = 'Q'
    elif self.value == 13:
      temp = 'K'

    if self.suit == 0:
      temp = temp + 'C'
    elif self.suit == 1:
      temp = temp + 'D'
    elif self.suit == 2:
      temp = temp + 'H'
    elif self.suit == 3:
      temp = temp + 'S'

    return temp

  