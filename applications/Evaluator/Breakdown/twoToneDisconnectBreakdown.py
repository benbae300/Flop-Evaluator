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

def twoToneDisconnectBreakdown(flop, range1, range2):
    breakDown = {
        'Nuts': 0,
        'All Straight Draws': 0,
        'Open-Ended Straight Draws': 0,
        'All Flush Draws': 0,
        'Nut Flush Draws': 0,
        'Flush Draws with 2 Overcards': 0,
        'Flush Draws with 1 Overcard': 0,
        'Straight and Flush Draws': 0,
        'Pairs with Flush Draws': 0,
        'All Pairs': 0,
        'Top Pair+': 0,
        'Strong Middling Pairs': 0,
        'Strong Bottom Pairs': 0,
        'Pairs with BDFDs': 0,
        'Overpairs': 0,
        'Strong Top Pairs': 0,
        'Middling Top Pairs': 0,
        'Weak Top Pairs': 0,
    }
    checkHandforPair = {
        0: ['Top Pair+'],
        1: ['Strong Middling Pairs'],
        2: ['Pairs with BDFDs'],
        3: ['Pairs with Flush Draws', 'All Flush Draws'],
        4: ['Strong Bottom Pairs'],
        5: ['Overpairs'],
        6: ['Strong Top Pairs'],
        7: ['Middling Top Pairs'],
        8: ['Weak Top Pairs']
    }
    checkHandforNonPair = {
        0: ['Nut Flush Draws'],
        1: ['Straight and Flush Draws'],
        2: ['Flush Draws with 2 Overcards'],
        3: ['Flush Draws with 1 Overcard'],
        4: ['Open-Ended Straight Draws'],
        5: ['All Straight Draws'],
        6: ['All Flush Draws']
    }
    range1Breakdown = copy.deepcopy(breakDown)
    range2Breakdown = copy.deepcopy(breakDown)
    flopVal = []
    totalWeight1 = 0
    totalWeight2 = 0
    frontSuit = ''
    backSuit = ''
    nutFlush = 0
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

    for h in range1.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyTwoToneDisconnect(hand, handClass, flopVal, frontSuit, backSuit, nutFlush)
        range1Breakdown = findBreakdown(res, range1Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight1 += weight

    for h in range2.returnRange():
        hand1, hand2, weight, handClass = h
        hand = [hand1, hand2]
        if handInFlop(hand, flop): continue
        res = classifyTwoToneDisconnect(hand, handClass, flopVal, frontSuit, backSuit, nutFlush)
        range2Breakdown = findBreakdown(res, range2Breakdown, checkHandforPair, checkHandforNonPair, weight)
        totalWeight2 += weight

    return finalDict(range1Breakdown, totalWeight1), finalDict(range2Breakdown, totalWeight2)

'''
bu, bb = BUBB2()
flop = [Card('A', 'h'), Card('K', 'h'), Card('J', 'c')]
BU, BB = twoToneDisconnectBreakdown(flop, bu, bb)
print(BU)
print(BB)
'''
