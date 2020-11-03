from . import getRange as g 
from . import RangeAnalyzer as r

def handVsRange(myPos, hand, pos1, pos2, action, flop):
    r1, r2 = g.getRange(pos1, pos2, action)
    ourHand = []
    villian = []

    if myPos == pos1: villian = r2
    else: villian = r1 

    card1 = hand[0]
    card1Val = card1.getValue()
    card1Suit = card1.suit

    card2 = hand[1]
    card2Val = card2.getValue()
    card2Suit = card2.suit

    if card1Val == card2Val: ourHand.append([card1, card2, 1, 'p'])
    elif card1Suit == card2Suit: ourHand.append([card1, card2, 1, 's'])
    else: ourHand.append([card1, card2, 1, 'o'])

    return r.RangeAnalyzer(ourHand, villian, flop)
    
'''
pos = 'UTG/HJ'
pos1 = 'BB'
pos2 = 'UTG/HJ'
action = '3BP'
flop = [Card('J', 'c'),Card('T', 'c'),Card('9', 'c')]
hand = [Card('7', 's'),Card('7', 'c') ]
print(handVsRange(pos, hand, pos1, pos2, action, flop))
'''
