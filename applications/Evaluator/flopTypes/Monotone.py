import sys
try:
    from .helper import *
except ModuleNotFoundError:
    from helper import *


'''
0: Strong Pairs + fd 
1: Strong Pairs no fd 
2: middle strong pair with fd
3: middle strong pair no fd  
4: Bottom pair  + fd
5: Bottom Pair + no fd 
6: pair with nut flush draw 
7: pair with strong flush draw
8: all fd 
'''
def classifyPair(hand, handVal, flopVal, flopSuit, handClass, nutFlush, strongFlush,  ):
    pair = 0
    other = 0
    middleStrong = []
    flopVal.sort()
    goodKicker = [14, 13, 12]
    pairDict = {'PAIR': [False, False, False, False, False, False, False, False, False]}
    maxPair = flopVal[2]
    middle = flopVal[1]
    for i in range(middle, maxPair):
        middleStrong.append(i)
    fd = hasSuit(hand, handClass, flopSuit )
    # get which card is the pair
    if handClass == 'p':
        pair = handVal[0]
        other = handVal[0]
    else:
        for h in handVal:
            if h in flopVal: pair = h
            else: other = h
    # start classsifying:

    if pair >= maxPair:
        if fd: pairDict['PAIR'][0] = True
        else: pairDict['PAIR'][1] = True
    elif handClass == 'p' and pair in middleStrong:
        if fd: pairDict['PAIR'][2] = True
        else: pairDict['PAIR'][3] = True
    elif pair == middle and other in goodKicker:
        if fd: pairDict['PAIR'][2] = True
        else: pairDict['PAIR'][3] = True
    elif pair in flopVal:
        if fd: pairDict['PAIR'][4] = True
        else: pairDict['PAIR'][5] = True
    else: pass
    if hand[0].suit == flopSuit:
        v = hand[0].getValue()
        if v == nutFlush: pairDict['PAIR'][6] = True
        if v in strongFlush: pairDict['PAIR'][7] = True
    elif hand[1].suit == flopSuit:
        v = hand[0].getValue()
        if v == nutFlush: pairDict['PAIR'][6] = True
        if v in strongFlush: pairDict['PAIR'][7] = True
    else: pass
    if fd: pairDict['PAIR'][8] = True
    return pairDict

'''
NonPairs:
- 0 all flush draws
- 1 Nut flush draws no pair 
- 2 strong flush draws no pair
'''
def classifyElse(hand, nutFlush, strongFlush, flopSuit):

    noPairDict = {'NOPAIR': [False, False, False]}
    if hand[0].suit == flopSuit:
        v = hand[0].getValue()
        noPairDict['NOPAIR'][0] = True
        if v == nutFlush: noPairDict['NOPAIR'][1] = True
        if v in strongFlush: noPairDict['NOPAIR'][2] = True
    elif hand[1].suit == flopSuit:
        v = hand[1].getValue()
        noPairDict['NOPAIR'][0] = True
        if v == nutFlush: noPairDict['NOPAIR'][1] = True
        if v in strongFlush: noPairDict['NOPAIR'][2] = True
    else: pass

    return noPairDict

def Monotone(hand, handClass, flopVal, flopSuit, nutFlush, strongFlush):
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
    if 2 in cardCounter.values() and len(reverse[2]) == 1 and not isFlush(hand, flopSuit):
        return classifyPair(hand, handVal, flopVal, flopSuit, handClass, nutFlush, strongFlush )
    elif 2 in cardCounter.values() or 3 in cardCounter.values() or isStraight(board) or isFlush(hand, flopSuit):
        return {'NUTS': [True]}
    else:
        return classifyElse(hand, nutFlush, strongFlush, flopSuit)

'''
hand = [Card('A','c'), Card('7', 'c')]
handClass = 's'
flopVal = [3, 5,  7]
flopSuit = 's'
nutFlush = 14
strongFlush = [13,12,11]

print(Monotone(hand, handClass, flopVal, flopSuit, nutFlush, strongFlush))
'''