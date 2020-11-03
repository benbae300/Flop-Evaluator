import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def BBCO3():
    co = r.Range()
    bb = r.Range()

    bb.addPair(11,14)
    bb.onePairCombo('T', 0.65)

    bb.oneSuitedCombo('K', 'J', 1)
    bb.oneSuitedCombo('J', 'T', 1)
    bb.oneSuitedCombo('Q', 'J', 1)
    bb.oneSuitedCombo('A', 'K', 1)
    bb.oneOffSuitCombo('A', 'K', 1)

    bb.oneSuitedCombo('A', '2', 0.2)
    bb.oneSuitedCombo('A', '3', 0.4)
    bb.oneSuitedCombo('A', '4', 0.5)
    bb.oneSuitedCombo('A', '5', 0.5)
    bb.oneSuitedCombo('A', 'Q', 0.1)
    bb.oneSuitedCombo('K', 'T', 0.8)
    bb.oneSuitedCombo('K', 'Q', 0.3)
    bb.oneSuitedCombo('Q', 'T', 0.9)
    bb.oneSuitedCombo('J', '9', 0.6)
    bb.oneSuitedCombo('T', '9', 0.6)
    bb.oneSuitedCombo('7', '6', 0.2)
    bb.oneSuitedCombo('6', '5', 0.4)

    bb.oneOffSuitCombo('A', 'J', 0.5)
    bb.oneOffSuitCombo('A', 'Q', 0.6)
    bb.oneOffSuitCombo('K', 'J', 0.3)
    bb.oneOffSuitCombo('K', 'Q', 0.2)

    ######
    co.addPair(9, 10)
    co.onePairCombo('J', 0.7)
    co.onePairCombo('Q', 0.3)
    co.onePairCombo('A', 0.6)

    co.onePairCombo('8', 0.8)
    co.onePairCombo('7', 0.7)
    co.onePairCombo('6', 0.5)
    co.onePairCombo('5', 0.3)
    co.onePairCombo('4', 0.2)

    co.addSuitedGivenFirstCard('A', 10, 12)
    co.oneSuitedCombo('A', 'K', 0.7)
    co.oneSuitedCombo('A', '9', 0.35)
    co.oneSuitedCombo('A', '8', 0.35)
    co.oneSuitedCombo('A', '7', 0.2)
    co.oneSuitedCombo('A', '5', 1)
    co.oneSuitedCombo('A', '4', 1)
    co.oneSuitedCombo('A', '3', 0.3)

    co.addSuitedGivenFirstCard('K', 10, 12)
    co.oneSuitedCombo('K', '6', 0.4)
    co.oneSuitedCombo('K', '9', 0.4)

    co.addSuitedGivenFirstCard('Q', 10, 11)
    co.addSuitedGivenFirstCard('J', 10, 10)
    co.oneSuitedCombo('J', '9', 0.3)
    co.oneSuitedCombo('T', '9', 0.5)
    co.oneSuitedCombo('8', '7', 0.5)
    co.oneSuitedCombo('7', '6', 0.45)
    co.oneSuitedCombo('6', '5', 0.2)
    co.oneSuitedCombo('5', '4', 0.5)

    co.oneOffSuitCombo('A', 'Q', 0.7)

    return bb, co 
