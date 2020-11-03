import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def BBBU3():
    bu = r.Range()
    bb = r.Range()
    
    bb.onePairCombo('8', 0.3)
    bb.onePairCombo('9', 0.7)
    bb.addPair(10,14)

    bb.oneSuitedCombo('A', 'Q', 1)
    bb.oneSuitedCombo('A', 'K', 1)
    bb.oneSuitedCombo('K', 'Q', 1)
    bb.oneOffSuitCombo('A', 'K', 1)

    bb.oneSuitedCombo('A', '2', 0.3)
    bb.oneSuitedCombo('A', '3', 0.25)
    bb.oneSuitedCombo('A', '4', 0.4)
    bb.oneSuitedCombo('A', '5', 0.5)
    bb.oneSuitedCombo('A', '6', 0.4)
    bb.oneSuitedCombo('A', '7', 0.4)
    bb.oneSuitedCombo('A', '8', 0.35)
    bb.oneSuitedCombo('A', '9', 0.35)
    bb.oneSuitedCombo('A', 'T', 0.5)
    bb.oneSuitedCombo('A', 'J', 0.5)

    bb.oneSuitedCombo('K', '9', 0.5)
    bb.oneSuitedCombo('K', 'T', 0.5)
    bb.oneSuitedCombo('K', 'J', 0.5)

    bb.oneSuitedCombo('Q', '9', 0.5)
    bb.oneSuitedCombo('Q', 'T', 0.5)
    bb.oneSuitedCombo('Q', 'J', 0.5)

    bb.oneSuitedCombo('J', '8', 0.5)
    bb.oneSuitedCombo('J', '9', 0.55)
    bb.oneSuitedCombo('J', 'T', 0.6)

    bb.oneSuitedCombo('T', '6', 0.4)
    bb.oneSuitedCombo('T', '7', 0.4)
    bb.oneSuitedCombo('T', '8', 0.5)
    bb.oneSuitedCombo('T', '9', 0.8)

    bb.oneSuitedCombo('9', '7', 0.4)
    bb.oneSuitedCombo('9', '8', 0.5)

    bb.oneSuitedCombo('8', '6', 0.3)
    bb.oneSuitedCombo('8', '7', 0.45)

    bb.oneSuitedCombo('6', '5', 0.3)
    bb.oneOffSuitCombo('A', 'T', 0.3)
    bb.oneOffSuitCombo('A', 'J', 0.7)
    bb.oneOffSuitCombo('A', 'Q', 0.7)

    bb.oneOffSuitCombo('K', 'T', 0.4)
    bb.oneOffSuitCombo('K', 'J', 0.4)
    bb.oneOffSuitCombo('K', 'Q', 0.6)
    #######
    bu.addPair(6,9)
    bu.onePairCombo('A', 1)
    bu.onePairCombo('T', 0.7)
    bu.onePairCombo('5', 0.7)
    bu.onePairCombo('4', 0.5)
    bu.onePairCombo('3', 0.2)
    bu.onePairCombo('2', 0.1)

    bu.addSuitedGivenFirstCard('A',8,13)
    bu.oneSuitedCombo('A','7',0.6)
    bu.oneSuitedCombo('A','6',0.6)
    bu.oneSuitedCombo('A','5',1)
    bu.oneSuitedCombo('A','4',1)
    bu.oneSuitedCombo('A','3',0.5)

    bu.addSuitedGivenFirstCard('K', 9, 11)
    bu.addSuitedGivenFirstCard('Q', 10, 11)
    bu.addSuitedGivenFirstCard('J', 10, 10)
    bu.addSuitedGivenFirstCard('T', 9, 9)

    bu.oneSuitedCombo('K','8',0.5)
    bu.oneSuitedCombo('K','7',0.5)
    bu.oneSuitedCombo('K','6',0.5)

    bu.oneSuitedCombo('Q','9',0.8)
    bu.oneSuitedCombo('J','9',0.8)
    bu.oneSuitedCombo('T','8',0.5)
    bu.oneSuitedCombo('9','8',0.5)
    bu.oneSuitedCombo('8','7',0.5)
    bu.oneSuitedCombo('7','6',0.5)
    bu.oneSuitedCombo('6','5',0.4)
    bu.oneSuitedCombo('5','4',0.6)

    bu.oneOffSuitCombo('K', 'Q', 0.6)
    bu.oneOffSuitCombo('K', 'J', 0.4)
    bu.oneOffSuitCombo('A', 'Q', 0.7)
    bu.oneOffSuitCombo('A', 'J', 0.6)
    return bb, bu 
