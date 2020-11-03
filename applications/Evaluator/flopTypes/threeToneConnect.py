import sys
try:
    from .helper import *
except ModuleNotFoundError:
    from helper import *

sys.path.insert(1, '../')

'''
0: strong pairs
1: pair + bdfd
2: bottom pair good kicker
3: pair + straight draw
4: overpair 
5: top pair good kicker 
6: top pair with straight draw 
7: middle pair good kicker
8: middle pair with straight draw 
'''
def classifyPair(hand, handVal, flopVal, flopSuit, handClass, straightCards):
    pair = 0
    other = 0
    pairDict = {'PAIR': [False, False, False, False, False, False, False, False, False]}
    flopVal.sort()
    goodKicker = [14,13,12]
    maxPair = flopVal[2]
    middle = flopVal[1]
    last = flopVal[0]
    middleStrong = []
    for i in range(middle, maxPair):
        middleStrong.append(i)

    # get which card is the pair
    if handClass == 'p':
        pair = handVal[0]
        other = handVal[0]
    else:
        for h in handVal:
            if h in flopVal: pair = h
            else: other = h
    # start classsifying:

    if pair >= maxPair: pairDict['PAIR'][0] = True

    if pair > maxPair: pairDict['PAIR'][4] = True 
    elif pair == maxPair and other in goodKicker: pairDict['PAIR'][5] = True 
    elif pair == maxPair and other in straightCards: pairDict['PAIR'][6] = True 
    elif pair == middle and other in goodKicker: pairDict['PAIR'][7] = True 
    elif pair in middleStrong and other in straightCards: pairDict['PAIR'][8] = True 
    elif pair == last and other in goodKicker: pairDict['PAIR'][2] = True
    else: pass

    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in flopSuit: pairDict['PAIR'][1] = True

    if other in straightCards: pairDict['PAIR'][3] = True
    return pairDict

'''
0: OESD
1: BDFD + straight draws
2: BDFD + 2 overcards
3: BDFD + 1 overcard
4: SD
5: BDFD
'''
def classifyElse(board, hand, handVal, handClass, flopVal, flopSuit, straightCards):
    maxFlop = max(flopVal)
    noPairDict = {'NOPAIR': [False, False, False, False, False, False ]}
    # start classifying:
    for h in handVal:
        if h in straightCards: noPairDict['NOPAIR'][4] = True

    if handClass == 's':
        handSuit = hand[0].suit
        if handSuit in flopSuit:
            noPairDict['NOPAIR'][5] = True

            if handVal[0] in straightCards or handVal[1] in straightCards: noPairDict['NOPAIR'][1] = True

            if handVal[0] > maxFlop and handVal[1] > maxFlop: noPairDict['NOPAIR'][2] = True
            elif handVal[0] > maxFlop or handVal[1] > maxFlop: noPairDict['NOPAIR'][3] = True
            else: pass


    if OESD(board) and 14 not in flopVal:
        noPairDict['NOPAIR'][0] = True
        noPairDict['NOPAIR'][4] = True
    return noPairDict

def classifyThreeToneConnect(hand, handClass, flopVal, flopSuit, straightCards):
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
        return classifyPair(hand, handVal, flopVal, flopSuit, handClass, straightCards)
    elif 2 in cardCounter.values() or 3 in cardCounter.values() or isStraight(board):
        return {'NUTS': [True]}
    else:
        return classifyElse(board, hand, handVal, handClass, flopVal, flopSuit, straightCards)


'''
hand = [Card('J', 's'), Card('9', 's')]
handClass = 's'
flopVal = [12,10,8]
flopSuit = ['c', 's', 'h']
sCards = ['3']
print(classifyThreeToneConnect(hand, handClass, flopVal, flopSuit, sCards))

'''