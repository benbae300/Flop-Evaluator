import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r
def BUBB2():
    bu = r.Range()
    bb = r.Range()
    bu.addPair(2,14)

    bu.addSuitedGivenFirstCard('A',2,13)
    bu.addSuitedGivenFirstCard('K', 2, 12)
    bu.addSuitedGivenFirstCard('Q', 3, 11)
    bu.addSuitedGivenFirstCard('J', 5, 10)
    bu.addSuitedGivenFirstCard('T', 6, 9)
    bu.addSuitedGivenFirstCard('9', 6, 8)
    bu.addSuitedGivenFirstCard('8', 6, 7)
    bu.addSuitedGivenFirstCard('7', 5, 6)

    bu.addOffSuitGivenFirstCard('A', 3, 13)
    bu.addOffSuitGivenFirstCard('K', 8, 12)
    bu.addOffSuitGivenFirstCard('Q', 9, 11)
    bu.addOffSuitGivenFirstCard('J', 9, 10)
    bu.addOffSuitGivenFirstCard('T', 8, 9)

    bu.oneSuitedCombo('J', '4', 0.5)
    bu.oneSuitedCombo('Q', '2', 0.5)
    bu.oneSuitedCombo('5', '4', 0.5)
    bu.oneSuitedCombo('6', '5', 0.9)

    bu.oneOffSuitCombo('J', '8', 0.5)
    bu.oneOffSuitCombo('9', '8', 0.5)

    ######
    bb.addPair(2,7)

    bb.addSuitedGivenFirstCard('K', 2, 8)
    bb.addSuitedGivenFirstCard('Q', 2, 8)
    bb.addSuitedGivenFirstCard('J', 4, 7)
    bb.addSuitedGivenFirstCard('9', 6, 6)
    bb.addSuitedGivenFirstCard('8', 5, 5)
    bb.addSuitedGivenFirstCard('7', 4, 5)
    bb.addSuitedGivenFirstCard('6', 4, 4)
    bb.addSuitedGivenFirstCard('5', 2, 4)
    bb.addSuitedGivenFirstCard('4', 2, 3)

    bb.oneSuitedCombo('A', '2', 0.7)
    bb.oneSuitedCombo('A', '3', 0.75)
    bb.oneSuitedCombo('A', '4', 0.6)
    bb.oneSuitedCombo('A', '5', 0.5)
    bb.oneSuitedCombo('A', '6', 0.6)
    bb.oneSuitedCombo('A', '7', 0.6)
    bb.oneSuitedCombo('A', '8', 0.65)
    bb.oneSuitedCombo('A', '9', 0.65)
    bb.oneSuitedCombo('A', 'T', 0.5)
    bb.oneSuitedCombo('A', 'J', 0.5)

    bb.oneSuitedCombo('K', '9', 0.5)
    bb.oneSuitedCombo('K', 'T', 0.5)
    bb.oneSuitedCombo('K', 'J', 0.5)

    bb.oneSuitedCombo('Q', '9', 0.5)
    bb.oneSuitedCombo('Q', 'T', 0.5)
    bb.oneSuitedCombo('Q', 'J', 0.5)

    bb.oneSuitedCombo('J', '8', 0.5)
    bb.oneSuitedCombo('J', '9', 0.45)
    bb.oneSuitedCombo('J', 'T', 0.4)

    bb.oneSuitedCombo('J', '2', 0.5)
    bb.oneSuitedCombo('J', '3', 0.5)

    bb.oneSuitedCombo('T', '6', 0.6)
    bb.oneSuitedCombo('T', '7', 0.6)
    bb.oneSuitedCombo('T', '8', 0.5)
    bb.oneSuitedCombo('T', '9', 0.2)

    bb.oneSuitedCombo('9', '7', 0.6)
    bb.oneSuitedCombo('9', '8', 0.5)

    bb.oneSuitedCombo('8', '6', 0.7)
    bb.oneSuitedCombo('8', '7', 0.65)

    bb.oneSuitedCombo('6', '5', 0.7)

    bb.addOffSuitGivenFirstCard('A',7,9)
    bb.addOffSuitGivenFirstCard('Q', 9, 11)
    bb.addOffSuitGivenFirstCard('J', 9, 10)
    bb.addOffSuitGivenFirstCard('A', 4, 5)

    bb.oneOffSuitCombo('A', '6', 0.5)

    bb.oneOffSuitCombo('A', 'T', 0.7)
    bb.oneOffSuitCombo('A', 'J', 0.3)
    bb.oneOffSuitCombo('A', 'Q', 0.3)

    bb.oneOffSuitCombo('K', 'T', 0.6)
    bb.oneOffSuitCombo('K', 'J', 0.6)
    bb.oneOffSuitCombo('K', 'Q', 0.4)

    bb.onePairCombo('8', 0.7)
    bb.onePairCombo('9', 0.3)

    return bu, bb




