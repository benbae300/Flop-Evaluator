import sys
from .helper import *
#sys.path.insert(1, '../')

'''
0: Strong pairs
1: Pair + bdfd
2: Lesser pairs on board
3: pairs+straight draws
4: Pairs + flush draws
5: overpair 
6: top pair good kicker 
7: top pair with straight draw 
8: middle pair good kicker
9: middle pair with straight draw 
'''
def classifyPair(hand, handVal, flopVal, frontSuit, backSuit, handClass, straightCards):
    pair = 0
    other = 0
    pairDict = {'PAIR': [False, False, False, False, False, False, False, False, False, False]}

    flopVal.sort()
    goodKicker = [14,13,12]
    maxPair = flopVal[2]
    middle = flopVal[1]
    last = flopVal[0]
    middleStrong = []
    for i in range(middle, maxPair):
        middleStrong.append(i)
    if handClass == 'p':
        pair = handVal[0]
        other = handVal[0]
        if hand[0].suit == frontSuit or hand[1].suit == frontSuit: pairDict['PAIR'][1] = True
    else:
        for h in handVal:
            if h in flopVal: pair = h
            else: other = h

    if pair >= maxPair: pairDict['PAIR'][0] = True

    if pair > maxPair: pairDict['PAIR'][5] = True 
    elif pair == maxPair and other in goodKicker: pairDict['PAIR'][6] = True 
    elif pair == maxPair and other in straightCards: pairDict['PAIR'][7] = True 
    elif pair == middle and other in goodKicker: pairDict['PAIR'][8] = True 
    elif pair in middleStrong and other in straightCards: pairDict['PAIR'][9] = True 
    elif pair == last and other in goodKicker: pairDict['PAIR'][2] = True
    else: pass
    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in frontSuit: pairDict['PAIR'][4] = True
        elif handSuit in backSuit: pairDict['PAIR'][1] = True
        else: pass

    if handClass == 'o':
        if hand[0].suit == frontSuit or hand[1].suit == frontSuit: pairDict['PAIR'][1] = True

    if other in straightCards: pairDict['PAIR'][3] = True
    return pairDict

'''
0: Nut flush draws
1: straight + flush draws 
2: open ended straight draws
3: Bdfd + straight draws (one -1 for last one, otherwise too weak)
4: all sd
5: all fd
'''
def classifyElse(board, hand, handVal, handClass, nutFlush, frontSuit, backSuit, straightCards, flopVal):

    noPairDict = {'NOPAIR': [False, False, False, False, False, False ]}
    for h in handVal:
        if h in straightCards: noPairDict['NOPAIR'][4] = True
    # if card is suited:
    if handClass == 's':
        handSuit = hand[0].suit
        # and that suit is the flopped fd:
        if handSuit in frontSuit:
            noPairDict['NOPAIR'][5] = True
            if handVal[0] in straightCards or handVal[1] in straightCards: noPairDict['NOPAIR'][1] = True
            if handVal[0] == nutFlush or handVal[1] == nutFlush: noPairDict['NOPAIR'][0] = True
        if handSuit in backSuit:
            if handVal[0] in straightCards or handVal[1] in straightCards: noPairDict['NOPAIR'][3] = True

    else:
        if hand[0].suit in frontSuit or hand[1].suit in frontSuit:
            if handVal[0] in straightCards or handVal[1] in straightCards: noPairDict['NOPAIR'][3] = True
    if OESD(board) and 14 not in flopVal: noPairDict['NOPAIR'][2] = True
    return noPairDict

def classifyTwoToneConnect(hand, handClass, flopVal, frontSuit, backSuit, nutFlush, straightCards):
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
        return classifyPair(hand, handVal, flopVal, frontSuit, backSuit, handClass, straightCards)
    elif 2 in cardCounter.values() or 3 in cardCounter.values() or isStraight(board):
        return {'NUTS': [True]}
    else:
        return classifyElse(board, hand, handVal, handClass, nutFlush, frontSuit, backSuit, straightCards, flopVal)

'''
hand = [Card('J', 's'), Card('T', 'c')]
handClass = 'o'
flopVal = [6,8,9]
frontSuit = 's'
backSuit = 'c'
nutFlush = 14
straightCards = [7, 10]
print(classifyTwoToneConnect(hand, handClass, flopVal, frontSuit, backSuit, nutFlush, straightCards))
'''
