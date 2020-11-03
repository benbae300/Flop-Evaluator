import sys
import glob
import copy
try:
    from .setStraight import *
    from .findBreakdown import *
except ModuleNotFoundError:
    from setStraight import *
    from findBreakdown import *

from applications.Evaluator.flopTypes import * 
from applications.Evaluator.allRanges import *

def handInFlop(hand, flop):
    for h in hand:
        for f in flop:
            if h.equalTo(f): return True
    return False

def monotoneBreakdown(flop, range1, range2,):
    breakDown = {
        'Nuts': 0,
        'All Pairs': 0,
        'Top Pair+ with Flush Draws': 0,
        'Top Pair+ with NO Flush Draws': 0,
        'Middling Pairs with Flush Draws': 0,
        'Midding Pairs with NO Flush Draws': 0,
        'Bottom Pairs with Flush Draws': 0,
        'Bottom Pairs with NO Flush Draws': 0,
        'Pairs with Nut Flush Draws': 0,
        'Pairs with Strong Flush Draws': 0,
        'All Flush Draws': 0,
        'Nut Flush Draw (NO Pair)': 0,
        'Strong Flush Draw (NO Pair)': 0
    }
    checkHandforPair = {
        0: ['Top Pair+ with Flush Draws'],
        1: ['Top Pair+ with NO Flush Draws'],
        2: ['Middling Pairs with Flush Draws'],
        3: ['Midding Pairs with NO Flush Draws'],
        4: ['Bottom Pairs with Flush Draws'],
        5: ['Bottom Pairs with NO Flush Draws'],
        6: ['Pairs with Nut Flush Draws'],
        7: ['Pairs with Strong Flush Draws'],
        8: ['All Flush Draws']
    }
    checkHandforNonPair = {
        0: ['All Flush Draws'],
        1: ['Nut Flush Draw (NO Pair)'],
        2: ['Strong Flush Draw (NO Pair)'],
    }
    range1Breakdown = copy.deepcopy(breakDown)
    range2Breakdown = copy.deepcopy(breakDown)
    totalWeight1 = 0
    totalWeight2 = 0
    flopVal = []
    flopSuit = ''
    nutFlush = 0
    strongFlush = []

    for f in flop:
        flopVal.append(f.getValue())
        flopSuit = f.suit
    flopVal.sort()
    for i in range(14, 9, -1):
        if i not in flopVal:
            nutFlush = i
            break
    getStrongFlush = flopVal[:]
    getStrongFlush.append(nutFlush)
    down = 14
    while(len(strongFlush) < 3 ):
        if down not in getStrongFlush: strongFlush.append(down)
        down -= 1
    for h in range1.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = Monotone(hand, handClass, flopVal, flopSuit, nutFlush, strongFlush)
        range1Breakdown = findBreakdown(res, range1Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight1 += weight

    for h in range2.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = Monotone(hand, handClass, flopVal, flopSuit, nutFlush, strongFlush)
        range2Breakdown = findBreakdown(res, range2Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight2 += weight


    return finalDict(range1Breakdown, totalWeight1), finalDict(range2Breakdown, totalWeight2)

'''
bu, bb = BUBB2()
flop = [Card('A', 'h'), Card('K', 'h'), Card('J', 'h')]
BU, BB = monotoneBreakdown(flop, bu, bb)
print(BU)
print(BB)
'''

