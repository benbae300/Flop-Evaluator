import sys
try:
    from .helper import *
except ModuleNotFoundError:
    from helper import *


'''
- 0 overpair 
- 1 underpair 
'''
def classifyPair(hand, flopNum):
    pairDict = {'PAIR': [False, False]}
    if hand[0].getValue() > flopNum:
        pairDict['PAIR'][0] = True
    else:
        pairDict['PAIR'][1] = True

    return pairDict
'''
- 0 2 overs  
- 1 1 over 
'''
def classifyElse(hand, flopNum):

    noPairDict = {'NOPAIR': [False, False, False, False, False, False ]}

    if hand[0].getValue() > flopNum and hand[1].getValue() > flopNum: noPairDict['NOPAIR'][0] = True
    elif hand[0].getValue() > flopNum or hand[1].getValue() > flopNum: noPairDict['NOPAIR'][1] = True
    else: pass
    return noPairDict

def classifyThreeSame(hand, handClass, flopNum):
    if hand[0].getValue() == flopNum or hand[1].getValue() == flopNum:
        return {'NUTS': [True]}
    elif handClass == 'p':
        return classifyPair(hand, flopNum)
    else:
        return classifyElse(hand, flopNum)


'''
hand = [Card('J', 's'), Card('J', 's')]
handClass = 'p'
flopNum = 2

print(classifyThreeSame(hand, handClass, flopNum))
'''