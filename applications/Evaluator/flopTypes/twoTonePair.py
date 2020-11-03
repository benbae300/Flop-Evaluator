import sys
try:
    from .helper import *
except ModuleNotFoundError:
    from helper import *




''' 
- 0 on board pair strong kicker 
- 1 on board pair weak kicker 
- 2 overpairs 
- 3 pair + bdfd
- 4 pair + FD 
'''
def classifyPair(hand, handVal, handClass, flopPair,flopVal, frontSuit, backSuit):
    pair = 0
    other = 0
    flopVal.sort()
    middleStrong = []
    goodKicker = [14, 13, 12]
    maxPair = flopVal[2]
    middle = flopVal[1]
    for i in range(middle, maxPair):
        middleStrong.append(i)
    pairDict = {'PAIR': [False, False, False, False, False]}
    if handClass == 'p':
        pair = handVal[0]
        other = handVal[0]
    else:
        for h in handVal:
            if h == flopPair:
                pair = h
            else:
                other = h
    if pair > flopPair: pairDict['PAIR'][2] = True
    elif pair == flopPair and other in goodKicker: pairDict['PAIR'][0] = True
    elif pair == flopPair: pairDict['PAIR'][1] = True
    else: pass
    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit == frontSuit: pairDict['PAIR'][4] = True
        if handSuit == backSuit: pairDict['PAIR'][3] = True
    else:
        if hand[0].suit == frontSuit or hand[1].suit == frontSuit: pairDict['PAIR'][3] = True

    return pairDict
''' 
-0: Nut Flush Draws
-1: All Flush Draws 
-2: Flush Draw + 2 overs 
-3: Flush draw + 1 over
'''
def classifyElse(board, hand, flopVal, handVal, handClass, nutFlush, frontSuit):

    noPairDict = {'NOPAIR': [False, False, False, False]}
    maxFlop = max(flopVal)
    # if card is suited:
    if handClass == 's':
        handSuit = hand[0].suit
        # and that suit is the flopped fd:
        if handSuit in frontSuit:
            noPairDict['NOPAIR'][1] = True
            if handVal[0] > maxFlop and handVal[1] > maxFlop: noPairDict['NOPAIR'][2] = True
            elif handVal[0] > maxFlop or handVal[1] > maxFlop: noPairDict['NOPAIR'][3] = True
            else: pass
            if handVal[0] == nutFlush or handVal[1] == nutFlush: noPairDict['NOPAIR'][0] = True

    return noPairDict

def classifyTwoTonePair(hand, handClass, flopVal, frontSuit, backSuit, flopPair, nutFlush):
    handVal = [hand[0].getValue(),hand[1].getValue()]
    board = flopVal[:]
    board += handVal
    cardCounter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    reverse = {}
    for val in (board):
        cardCounter[val] += 1
    for key, value in cardCounter.items():
        reverse.setdefault(value, list()).append(key)
    board.sort()
    if 2 in cardCounter.values() and  len(reverse[2]) == 2:
        return classifyPair(hand, handVal, handClass, flopPair,flopVal, frontSuit, backSuit)
    elif 4 in cardCounter.values() or 3 in cardCounter.values():
        return {'NUTS': [True]}
    else:
        return classifyElse(board, hand, flopVal, handVal, handClass, nutFlush, frontSuit)

'''
hand = [Card('4', 's'), Card('6', 's')]
handClass = 's'
flopVal = [2,2,3]
frontSuit = 's'
backSuit = 'c'
nutFlush = 14
flopPair = 2
print(classifyTwoTonePair(hand, handClass, flopVal, frontSuit, backSuit, flopPair, nutFlush))
'''

