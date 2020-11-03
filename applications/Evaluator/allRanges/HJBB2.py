import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def HJBB2():
    hj = r.Range()
    bb = r.Range()

    hj.addPair(6, 14)
    hj.onePairCombo('5',0.5)
    hj.onePairCombo('4', 0.5)
    hj.onePairCombo('3', 0.5)
    hj.onePairCombo('2', 0.5)

    hj.addSuitedGivenFirstCard('A', 2, 13)
    hj.addSuitedGivenFirstCard('K', 5, 12)
    hj.addSuitedGivenFirstCard('Q', 8, 11)
    hj.addSuitedGivenFirstCard('J', 9, 10)
    hj.addSuitedGivenFirstCard('T', 9, 9)

    hj.oneSuitedCombo('9', '8', 0.3)
    hj.oneSuitedCombo('8', '7', 0.35)
    hj.oneSuitedCombo('7', '6', 0.3)
    hj.oneSuitedCombo('6', '5', 0.2)
    hj.oneSuitedCombo('5', '4', 0.4)

    hj.addOffSuitGivenFirstCard('A', 10, 13)
    hj.addOffSuitGivenFirstCard('K', 10, 12)
    hj.addOffSuitGivenFirstCard('Q', 11, 11)

    hj.oneOffSuitCombo('A', '9', 0.5)
    hj.oneOffSuitCombo('Q', 'T', 0.65)
    ########

    bb.addPair(2,10)
    bb.onePairCombo('J', 0.3)

    bb.addSuitedGivenFirstCard('K', 2, 4)
    bb.addSuitedGivenFirstCard('K', 7, 9)
    bb.addSuitedGivenFirstCard('Q', 5, 9)
    bb.addSuitedGivenFirstCard('J', 7, 9)
    bb.addSuitedGivenFirstCard('T', 7, 9)
    bb.addSuitedGivenFirstCard('9', 6, 8)
    bb.addSuitedGivenFirstCard('8', 5, 6)
    bb.addSuitedGivenFirstCard('7', 4, 5)
    bb.addSuitedGivenFirstCard('6', 4, 4)
    bb.addSuitedGivenFirstCard('5', 3, 3)
    bb.addSuitedGivenFirstCard('4', 3, 3)

    bb.oneSuitedCombo('K', '5', 0.55)
    bb.oneSuitedCombo('K', '6', 0.6)
    bb.oneSuitedCombo('Q', '4', 0.4)
    bb.oneSuitedCombo('Q', 'T', 0.4)
    bb.oneSuitedCombo('J', 'T', 0.5)
    bb.oneSuitedCombo('8', '7', 0.65)
    bb.oneSuitedCombo('7', '6', 0.65)
    bb.oneSuitedCombo('6', '5', 0.55)
    bb.oneSuitedCombo('5', '4', 0.55)
    bb.oneSuitedCombo('6', '3', 0.5)
    bb.oneSuitedCombo('5', '2', 0.5)
    bb.oneSuitedCombo('4', '2', 0.5)

    bb.addOffSuitGivenFirstCard('A', 10, 11)
    bb.oneOffSuitCombo('A', 'Q', 0.55)
    bb.oneOffSuitCombo('A', '9', 0.5)

    bb.addOffSuitGivenFirstCard('K', 10, 12)
    bb.addOffSuitGivenFirstCard('Q', 12, 12)
    bb.oneOffSuitCombo('Q', 'T', 0.5)
    bb.oneOffSuitCombo('J', 'T', 0.5)

    return hj, bb


