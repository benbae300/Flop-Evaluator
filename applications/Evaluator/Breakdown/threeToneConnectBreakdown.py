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

def threeToneConnectBreakdown(flop, range1, range2):
    breakDown ={
        'Nuts': 0,
        'All Straight Draws': 0,
        'Open-Ended Straight Draws': 0,
        'Pairs with Straight Draws': 0,
        'BDFDs with Straight Draws': 0,
        'All BDFDs': 0,
        'BDFDs with 2 overcards': 0,
        'BDFDs with 1 overcard': 0,
        'BDFDs with Pairs': 0,
        'All Pairs': 0,
        'Top Pair+': 0,
        'Strong Bottom Pairs': 0,
        'Overpairs': 0,
        'Strong Top Pairs': 0,
        'Top Pairs with Straight Draws': 0,
        'Strong Middling Pairs': 0,
        'Middling Pairs with Straight Draws': 0
    }
    checkHandforPair = {
        0: ['Top Pair+'],
        1: ['BDFDs with Pairs', 'All BDFDs'],
        2: ['Strong Bottom Pairs'],
        3: ['Pairs with Straight Draws', 'All Straight Draws'],
        4: ['Overpairs'],
        5: ['Strong Top Pairs'],
        6: ['Top Pairs with Straight Draws'],
        7: ['Strong Middling Pairs'],
        8: ['Middling Pairs with Straight Draws']
    }
    checkHandforNonPair = {
        0: ['Open-Ended Straight Draws'],
        1: ['BDFDs with Straight Draws'],
        2: ['BDFDs with 2 overcards'],
        3: ['BDFDs with 1 overcard'],
        4: ['All Straight Draws'],
        5: ['All BDFDs']
    }
    # if pair and if check[0]: breakDown[checkHandforPair[0]] += weight
    range1Breakdown = copy.deepcopy(breakDown)
    range2Breakdown = copy.deepcopy(breakDown)
    flopVal = []
    flopSuit = []
    totalWeight1 = 0
    totalWeight2 = 0
    for f in flop:
        flopVal.append(f.getValue())
        flopSuit.append(f.suit)
    straightCards = setStraight(flopVal)

    for h in range1.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyThreeToneConnect(hand, handClass, flopVal, flopSuit, straightCards)
        range1Breakdown = findBreakdown(res, range1Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight1 += weight

    for h in range2.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyThreeToneConnect(hand, handClass, flopVal, flopSuit, straightCards)
        range2Breakdown = findBreakdown(res, range2Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight2 += weight
    return finalDict(range1Breakdown, totalWeight1), finalDict(range2Breakdown, totalWeight2)

'''
bu, bb = BUBB2()
flop = [Card('A', 's'), Card('K', 's'), Card('J', 'c')]
BU, BB = threeToneConnectBreakdown(flop, bu, bb)
print(BU)
print(BB)
'''

