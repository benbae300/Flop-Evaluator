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
def threeSameBreakdown(flop, range1, range2):
    breakDown = {
        'Nuts': 0,
        'All Pairs': 0,
        'Overpairs': 0,
        'Underpairs': 0,
        '2 Overcards': 0,
        '1 Overcard': 0
    }
    checkHandforPair = {
        0: ['Overpairs'],
        1: ['Underpairs']
    }
    checkHandforNonPair = {
        0: ['2 Overcards'],
        1: ['1 Overcard']
    }
    range1Breakdown = copy.deepcopy(breakDown)
    range2Breakdown = copy.deepcopy(breakDown)
    flopNum = flop[0].getValue()
    totalWeight1 = 0
    totalWeight2 = 0


    for h in range1.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyThreeSame(hand, handClass, flopNum)
        range1Breakdown = findBreakdown(res, range1Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight1 += weight
    for h in range2.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyThreeSame(hand, handClass, flopNum)
        range2Breakdown = findBreakdown(res, range2Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight2 += weight
    return finalDict(range1Breakdown, totalWeight1), finalDict(range2Breakdown, totalWeight2)


'''
bu, bb = BUBB2()
flop = [Card('4', 'h'), Card('4', 's'), Card('4', 'c')]
BU, BB = threeSameBreakdown(flop, bu, bb)
print(BU)
print(BB)
'''
