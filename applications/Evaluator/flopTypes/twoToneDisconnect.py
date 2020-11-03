import sys
try:
    from .helper import *
except ModuleNotFoundError:
    from helper import *



'''
PAIRS:
- 0 strong pairs
- 1 strong middling pair 
- 2 pair + bdfd
- 3 pair + FD
- 4 bottom pair good kicker
- 5 overpairs 
- 6 strong top pairs 
- 7 middle top pairs
- 8 weak top pairs 
'''
def classifyPair(hand, handVal, flopVal, frontSuit, backSuit, handClass):
    pair = 0
    other = 0
    middleStrong = []
    flopVal.sort()
    goodKicker = [14, 13, 12]
    midKicker = [11,10,9,8]
    pairDict = {'PAIR': [False, False, False, False, False, False, False, False, False]}
    maxPair = flopVal[2]
    middle = flopVal[1]
    last = flopVal[0]
    for i in range(middle, maxPair):
        middleStrong.append(i)
    if handClass == 'p':
        pair = handVal[0]
        other = handVal[0]
        if hand[0].suit == frontSuit or hand[1].suit == frontSuit:
            pairDict['PAIR'][2] = True

    else:
        for h in handVal:
            if h in flopVal:
                pair = h
            else:
                other = h
    if pair >= maxPair: pairDict['PAIR'][0] = True

    if pair > maxPair: pairDict['PAIR'][5] = True 
    elif pair == maxPair and other in goodKicker: pairDict['PAIR'][6] = True 
    elif pair == maxPair and other in midKicker: pairDict['PAIR'][7] = True 
    elif pair == maxPair: pairDict['PAIR'][8] = True 
    elif handClass == 'p' and pair in middleStrong: pairDict['PAIR'][1] = True
    elif pair == middle and other in goodKicker: pairDict['PAIR'][1] = True
    elif pair == last and other in goodKicker: pairDict['PAIR'][4] = True
    else: pass


    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in frontSuit: pairDict['PAIR'][3] = True
        elif handSuit in backSuit: pairDict['PAIR'][2] = True
        else: pass
    elif handClass == 'o':
        if hand[0].suit == frontSuit or hand[1].suit == frontSuit: pairDict['PAIR'][2] = True
    return pairDict
'''
NonPairs:
- 0 Nut flush draws
- 1 straight + flush draws 
- 2 flush + 2 overs 
- 3 flush + 1 over 
- 4 open ended straight draws
- 5 all sd
- 6 all fd
'''
def classifyElse(board, hand, flopVal, handVal, handClass, nutFlush, frontSuit):

    noPairDict = {'NOPAIR': [False, False, False, False, False, False, False ]}
    isStraight = straightDraw(board)
    maxFlop = max(flopVal)
    if isStraight: noPairDict['NOPAIR'][5] = True
    # if card is suited:
    if handClass == 's':
        handSuit = hand[0].suit
        # and that suit is the flopped fd:
        if handSuit in frontSuit:
            noPairDict['NOPAIR'][6] = True
            if handVal[0] > maxFlop and handVal[1] > maxFlop: noPairDict['NOPAIR'][2] = True
            elif handVal[0] > maxFlop or handVal[1] > maxFlop: noPairDict['NOPAIR'][3] = True
            else: pass
            if isStraight: noPairDict['NOPAIR'][1] = True
            if handVal[0] == nutFlush or handVal[1] == nutFlush: noPairDict['NOPAIR'][0] = True

    if OESD(board): noPairDict['NOPAIR'][4] = True
    return noPairDict

def classifyTwoToneDisconnect(hand, handClass, flopVal, frontSuit, backSuit, nutFlush):
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
        return classifyPair(hand, handVal, flopVal, frontSuit, backSuit, handClass)
    elif 2 in cardCounter.values() or 3 in cardCounter.values():
        return {'NUTS': [True]}
    else:
        return classifyElse(board, hand, flopVal, handVal, handClass, nutFlush, frontSuit)

'''
hand = [Card('9', 's'), Card('9', 'h')]
handClass = 'p'
flopVal = [13,2,3]
frontSuit = 's'
backSuit = 'c'
nutFlush = 14
print(classifyTwoToneDisconnect(hand, handClass, flopVal, frontSuit, backSuit, nutFlush))
'''
