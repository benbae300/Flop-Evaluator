import sys
try:
    from .helper import *
except ModuleNotFoundError:
    from helper import *



'''
- 0 strong pairs (top pair +)
- 1 strong middling pair 
- 2 pair + bdfd
- 3 bottom pair good kicker
- 4 overpairs 
- 5 strong top pairs 
- 6 middle top pairs
- 7 weak top pairs 
'''
def classifyPair(hand, handVal, flopVal, flopSuit, handClass):
    pair = 0
    other = 0
    flopVal.sort()
    middleStrong = []
    goodKicker = [14,13,12]
    midKicker = [11,10,9,8]
    pairDict = {'PAIR': [False, False, False, False, False, False, False, False]}
    maxPair = flopVal[2]
    middle = flopVal[1]
    last = flopVal[0]
    for i in range(middle, maxPair):
        middleStrong.append(i)
    if handClass == 'p':
        pair = handVal[0]
        other = handVal[0]
    else:
        for h in handVal:
            if h in flopVal:
                pair = h
            else:
                other = h
    if pair >= maxPair: pairDict['PAIR'][0] = True

    if pair > maxPair: pairDict['PAIR'][4] = True 
    elif pair == maxPair and other in goodKicker: pairDict['PAIR'][5] = True 
    elif pair == maxPair and other in midKicker: pairDict['PAIR'][6] = True 
    elif pair == maxPair: pairDict['PAIR'][7] = True 
    elif handClass == 'p' and pair in middleStrong: pairDict['PAIR'][1] = True
    elif pair == middle and other in goodKicker: pairDict['PAIR'][1] = True
    elif pair == last and other in goodKicker: pairDict['PAIR'][3] = True
    else: pass
    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in flopSuit: pairDict['PAIR'][2] = True
    return pairDict

'''
- 0 OESD check 
- 1 BDFD + straight draws
- 2 BDFD + 2 overcards check 
- 3 BDFD + 1 overcard check 
- 4 SD
- 5 BDFD check 
'''
def classifyElse(board, hand, handVal, handClass, flopVal, flopSuit):
    maxFlop = max(flopVal)
    noPairDict = {'NOPAIR': [False, False, False, False, False, False ]}
    isStraight = straightDraw(board)
    if isStraight: noPairDict['NOPAIR'][4] = True
    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in flopSuit:
            noPairDict['NOPAIR'][5] = True

            if isStraight: noPairDict['NOPAIR'][1] = True

            if handVal[0] > maxFlop and handVal[1] > maxFlop: noPairDict['NOPAIR'][2] = True
            elif handVal[0] > maxFlop or handVal[1] > maxFlop: noPairDict['NOPAIR'][3] = True
            else: pass

    if OESD(board): noPairDict['NOPAIR'][0] = True
    return noPairDict

def classifyThreeToneDisconnect(hand, handClass, flopVal, flopSuit):
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
    if 2 in cardCounter.values() and len(reverse[2]) == 1:
        return classifyPair(hand, handVal, flopVal, flopSuit, handClass)
    elif 2 in cardCounter.values() or 3 in cardCounter.values():
        return {'NUTS': [True]}
    else:
        return classifyElse(board, hand, handVal, handClass, flopVal, flopSuit)

'''
hand = [Card('J', 's'), Card('4', 's')]
handClass = 's'
flopVal = [14,2,3]
flopSuit = ['c', 's', 'h']
print(classifyThreeToneDisconnect(hand, handClass, flopVal, flopSuit))
'''

