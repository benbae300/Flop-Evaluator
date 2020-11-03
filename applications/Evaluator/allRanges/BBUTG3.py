import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def BBUTG3():
    utg = r.Range()
    bb  = r.Range()
    bb.addPair(12,14)
    bb.onePairCombo('J', 0.1)

    bb.oneSuitedCombo('A', '2', 0.1)
    bb.oneSuitedCombo('A', '3', 0.4)
    bb.oneSuitedCombo('A', '4', 0.5)
    bb.oneSuitedCombo('A', '5', 0.45)
    bb.oneSuitedCombo('A', 'T', 0.5)
    bb.oneSuitedCombo('A', 'J', 0.4)
    bb.oneSuitedCombo('A', 'Q', 0.7)

    bb.oneSuitedCombo('K', '5', 0.55)
    bb.oneSuitedCombo('K', '6', 0.5)
    bb.oneSuitedCombo('K', '7', 0.35)
    bb.oneSuitedCombo('K', 'T', 0.4)
    bb.oneSuitedCombo('K', 'J', 0.8)
    bb.oneSuitedCombo('K', 'Q', 1)

    bb.oneSuitedCombo('Q', 'T', 0.4)
    bb.oneSuitedCombo('Q', 'J', 0.6)

    bb.oneSuitedCombo('9', '8', 0.2)
    bb.oneSuitedCombo('8', '7', 0.2)
    bb.oneSuitedCombo('7', '6', 0.45)
    bb.oneSuitedCombo('6', '5', 0.5)

    bb.oneOffSuitCombo('A', 'Q', 0.2)
    bb.oneOffSuitCombo('A', 'K', 0.75)
    #####
    utg.onePairCombo('A', 0.2)
    utg.onePairCombo('K', 0.35)
    utg.onePairCombo('Q', 1)
    utg.onePairCombo('J', 0.9)
    utg.onePairCombo('T', 0.5)
    utg.onePairCombo('9', 0.5)
    utg.onePairCombo('8', 0.4)
    utg.onePairCombo('7', 0.5)
    utg.onePairCombo('6', 0.25)
    utg.onePairCombo('5', 0.2)
    utg.onePairCombo('4', 0.17)

    utg.oneSuitedCombo('A', 'K', 0.55)
    utg.oneSuitedCombo('A', '5', 0.8)
    utg.oneSuitedCombo('A', '4', 0.5)
    utg.addSuitedGivenFirstCard('A', 10, 12)

    utg.oneSuitedCombo('K', 'Q', 1)
    utg.oneSuitedCombo('K', 'J', 0.9)
    utg.oneSuitedCombo('K', 'T', 0.45)
    utg.oneSuitedCombo('Q', 'T', 0.1)
    utg.oneSuitedCombo('J', 'T', 0.3)
    utg.oneSuitedCombo('T', '9', 0.5)

    utg.oneSuitedCombo('8', '7', 0.3)
    utg.oneSuitedCombo('7', '6', 0.3)
    utg.oneSuitedCombo('6', '5', 0.3)
    utg.oneSuitedCombo('5', '4', 0.3)

    utg.oneOffSuitCombo('A', 'K', 0.25)

    return bb, utg 