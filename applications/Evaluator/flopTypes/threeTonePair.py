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
'''
def classifyPair(hand, handVal, handClass, flopPair,flopVal, flopSuit):
    pair = 0
    other = 0
    flopVal.sort()
    middleStrong = []
    goodKicker = [14, 13, 12]
    maxPair = flopVal[2]
    middle = flopVal[1]
    for i in range(middle, maxPair):
        middleStrong.append(i)
    pairDict = {'PAIR': [False, False, False, False]}
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
        if handSuit in flopSuit: pairDict['PAIR'][3] = True
    return pairDict
''' 
- 0 2 overcard + bdfd 
- 1 1 overcard + bdfd 
- 2 all Bdfd  
'''
def classifyElse(hand, handVal, handClass, flopVal, flopSuit):
    maxFlop = max(flopVal)
    noPairDict = {'NOPAIR': [False, False, False ]}
    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in flopSuit:
            noPairDict['NOPAIR'][2] = True
            if handVal[0] > maxFlop and handVal[1] > maxFlop: noPairDict['NOPAIR'][0] = True
            elif handVal[0] > maxFlop or handVal[1] > maxFlop: noPairDict['NOPAIR'][1] = True
            else: pass

    return noPairDict


def classifyThreeTonePair(hand, handClass, flopVal, flopSuit, flopPair):
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
        return classifyPair(hand, handVal, handClass, flopPair,flopVal, flopSuit)
    elif 4 in cardCounter.values() or 3 in cardCounter.values():
        return {'NUTS': [True]}
    else:
        return classifyElse(hand, handVal, handClass, flopVal, flopSuit)

'''
hand = [Card('A', 's'), Card('9', 's')]
handClass = 's'
flopPair = 9
flopVal = [6,6,9]
flopSuit = ['s', 'c', 'h']

print(classifyThreeTonePair(hand, handClass, flopVal, flopSuit, flopPair))
'''
