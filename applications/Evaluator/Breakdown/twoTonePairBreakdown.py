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
def twoTonePairBreakdown(flop, range1, range2):
    breakDown = {
        'Nuts': 0,
        'All Flush Draws': 0,
        'Nut Flush Draws': 0,
        'Flush Draws with 2 overcards': 0,
        'Flush Draws with 1 overcard': 0,
        'Pairs with Flush Draws': 0,
        'Pairs with BDFDs': 0,
        'All Pairs': 0,
        'Strong Pairs on Board': 0,
        'Weak Pairs on Board': 0,
        'Overpairs': 0
    }
    checkHandforPair = {
        0: ['Strong Pairs on Board'],
        1: ['Weak Pairs on Board'],
        2: ['Overpairs'],
        3: ['Pairs with BDFDs' ],
        4: ['Pairs with Flush Draws', 'All FDs']
    }
    checkHandforNonPair = {
        0: ['Nut Flush Draws'],
        1: ['All Flush Draws'],
        2: ['Flush Draws with 2 overcards'],
        3: ['Flush Draws with 1 overcard']
    }
    range1Breakdown = copy.deepcopy(breakDown)
    range2Breakdown = copy.deepcopy(breakDown)
    flopVal = []
    flopSuit = []
    flopPair = 0
    nutFlush = 0
    frontSuit = ''
    backSuit = ''
    totalWeight1 = 0
    totalWeight2 = 0
    suits = {'c': [0, []], 'd': [0, []], 'h': [0, []], 's': [0, []]}
    for f in flop:
        flopVal.append(f.getValue())
        suits[f.suit][0] += 1
        suits[f.suit][1].append(f.getValue())
    for key in suits:
        if suits[key][0] == 2:
            frontSuit = key
        if suits[key][0] == 1:
            backSuit = key
    flushValues = suits[frontSuit][1]

    for i in range(14, 9, -1):
        if i not in flushValues:
            nutFlush = i
            break
    v = []
    for val in flopVal:
        if val not in v:
            v.append(val)
        else:
            v.remove(val)
    flopPair = v[0]

    for h in range1.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyTwoTonePair(hand, handClass, flopVal, frontSuit, backSuit, flopPair, nutFlush)
        range1Breakdown = findBreakdown(res, range1Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight1 += weight
    for h in range2.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyTwoTonePair(hand, handClass, flopVal, frontSuit, backSuit, flopPair, nutFlush)
        range2Breakdown = findBreakdown(res, range2Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight2 += weight
    return finalDict(range1Breakdown, totalWeight1), finalDict(range2Breakdown, totalWeight2)

'''
bu, bb = BUBB2()
flop = [Card('A', 's'), Card('3', 's'), Card('3', 'c')]
BU, BB = twoTonePairBreakdown(flop, bu, bb)
print(BU)
print(BB)
'''
