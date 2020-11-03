import sys
sys.path.append('/Breakdown')
from . import classifyFlop as classify
from . import getRange as getRange
from .Breakdown import *



def breakdownTheRange(action, range1, range2, flop):
    r1, r2 = getRange.getRange(range1, range2, action)
    flopType = classify.classify(flop)
    if flopType == 1: return threeToneConnectBreakdown(flop, r1, r2)
    elif flopType == 2: return twoToneConnectBreakdown(flop, r1, r2)
    elif flopType == 3: return threeToneDisconnectBreakdown(flop, r1, r2)
    elif flopType == 4: return twoToneDisconnectBreakdown(flop, r1, r2)
    elif flopType == 5: return monotoneBreakdown(flop, r1, r2)
    elif flopType == 6: return threeTonePairBreakdown(flop, r1, r2)
    elif flopType == 7: return twoTonePairBreakdown(flop, r1, r2)
    elif flopType == 8: return threeSameBreakdown(flop, r1, r2)


'''
action ='3BP'
range1 = 'BU'
range2 = 'CO'
flop = [Card('A', 's'), Card('3', 's'), Card('2', 's')]
a,b = breakdownTheRange(action, range1, range2, flop)
print(a)
print(b)
'''


