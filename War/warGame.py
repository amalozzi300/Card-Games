import card as c
import deck as d

def Winner(p1, p2):
  # adjusts values to make ace high
  p1Value = p1.value
  if p1Value == 1:
    p1Value = 13

  p2Value = p2.value
  if p2Value == 1:
    p2Value = 13

  if p1Value > p2Value:
    return 1
  elif p2Value > p1Value:
    return 2
  else:
    return 0

def CardsWon(cards):
  temp = ''

  for i in range(len(cards)):
    temp = temp + str(cards[i])

    if i != len(cards) - 1:
      temp = temp + ', '

  return temp

if __name__ == '__main__':
  run = True
  cards = d.Deck()
  p1Cards = []
  p2Cards = []
  playedCards = []

  while run:
    run = False
    p1Lose = False
    p2Lose = False

    cards.Shuffle()

    # deals cards to start game
    for i in range(52):
      if i % 2 == 1:
        p1Cards.append(cards[i])
      else:
        p2Cards.append(cards[i])

    while len(p1Cards) != 0 and len(p2Cards) != 0:
      p1 = p1Cards.pop(0)
      p2 = p2Cards.pop(0)

      playedCards.clear()
      playedCards.append(p1)
      playedCards.append(p2)

      winner = Winner(p1, p2)

      print('Player 1 shows: ' + str(p1))
      print('Player 2 shows: ' + str(p2))
      print()

      if winner == 1:
        print('Player 1 wins!\n')
        cardsWon = CardsWon(playedCards)
        print(cardsWon +  ' have been added to their deck!\n')

        for i in range (len(playedCards)):
          p1Cards.append(playedCards[i])

      elif winner == 2:
        print('Player 2 wins!\n')
        cardsWon = CardsWon(playedCards)
        print(cardsWon +  ' have been added to their deck!\n')

        for i in range (len(playedCards)):
          p2Cards.append(playedCards[i])

      else:
        while winner == 0 or (p1Lose or p2Lose):
          print('Draw.')
          print('Prepare for War!\n')
          input('Press \'Enter\' to go to war!')
          print()

          if len(p1Cards) > 1:
            playedCards.append(p1Cards.pop(0))
            p1 = p1Cards.pop(0)
            playedCards.append(p1)
          elif len(p1Cards) == 1:
            p1 = p1Cards.pop(0)
            playedCards.append(p1)  
          else:
            p1Lose = True
            print('Player 1 Does Not Have Enough Cards.')

          if len(p2Cards) > 1:
            playedCards.append(p2Cards.pop(0))
            p2 = p2Cards.pop(0)
            playedCards.append(p2)
          elif len(p2Cards) == 1:
            p2 = p2Cards.pop(0)
            playedCards.append(p2)  
          else:
            p2Lose = True           
            print('Player 2 Does Not Have Enough Cards.')

          if not p1Lose and not p2Lose:
            winner = Winner(p1, p2)

            print('Player 1 shows: ' + str(p1))
            print('Player 2 shows: ' + str(p2))
            print()

            if winner == 1:
              print('Player 1 wins!\n')
              cardsWon = CardsWon(playedCards)
              print(cardsWon +  ' have been added to their deck!\n')

              for i in range (len(playedCards)):
                p1Cards.append(playedCards[i])

            elif winner == 2:
              print('Player 2 wins!\n')
              cardsWon = CardsWon(playedCards)
              print(cardsWon +  ' have been added to their deck!\n')

              for i in range (len(playedCards)):
                p2Cards.append(playedCards[i])

      if len(p1Cards) != 0 and len(p2Cards) != 0:
        print('Current Scores:')
        print('Player 1: ' + str(len(p1Cards)))
        print('Player 2: ' + str(len(p2Cards)))
        print()
        input('Press \'Enter\' to continue')
        print()

    if len(p1Cards) == 0:
      print('Player 1 is out of cards')
      print('Player 1 loses.')
    else:
      print('Player 2 is out of cards')
      print('Player 2 loses.')

    again = input('Would you like to play again? (y / n): ')

    while again != 'y' and again != 'Y' and again != 'n' and again != 'N':
      print('\nInvalid Choice. Please try again.')
      again = input('Would you like to play again? (y / n): ')

    if again == 'y' or again == 'Y':
      run = True

