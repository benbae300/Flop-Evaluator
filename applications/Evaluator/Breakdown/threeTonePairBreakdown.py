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
def threeTonePairBreakdown(flop, range1, range2):
    breakDown = {
        'Nuts': 0,
        'All BDFDs': 0,
        'BDFDs with 2 overcards': 0,
        'BDFDs with 1 overcard': 0,
        'BDFDs with Pairs': 0,
        'All Pairs': 0,
        'Strong Pairs on Board': 0,
        'Weak Pairs on Board': 0,
        'OverPairs': 0,
    }
    checkHandforPair = {
        0: ['Strong Pairs on Board'],
        1: ['Weak Pairs on Board'],
        2: ['OverPairs'],
        3: ['BDFDs with Pairs','All BDFDs' ]
    }
    checkHandforNonPair = {
        0: ['BDFDs with 2 overcards'],
        1: ['BDFDs with 1 overcard'],
        2: ['All BDFDs']
    }
    range1Breakdown = copy.deepcopy(breakDown)
    range2Breakdown = copy.deepcopy(breakDown)
    flopVal = []
    flopSuit = []
    flopPair = 0
    totalWeight1 = 0
    totalWeight2 = 0
    for f in flop:
        flopVal.append(f.getValue())
        flopSuit.append(f.suit)
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
        res = classifyThreeTonePair(hand, handClass, flopVal, flopSuit, flopPair)
        range1Breakdown = findBreakdown(res, range1Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight1 += weight
    for h in range2.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyThreeTonePair(hand, handClass, flopVal, flopSuit, flopPair)
        range2Breakdown = findBreakdown(res, range2Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight2 += weight
    return finalDict(range1Breakdown, totalWeight1), finalDict(range2Breakdown, totalWeight2)

'''
bu, bb = BUBB2()
flop = [Card('A', 'h'), Card('3', 's'), Card('3', 'c')]
BU, BB = threeTonePairBreakdown(flop, bu, bb)
print(BU)
print(BB)
'''
