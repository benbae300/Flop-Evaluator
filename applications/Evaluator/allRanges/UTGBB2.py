import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def UTGBB2():
    utg = r.Range()
    bb  = r.Range()

    utg.addPair(7, 14)
    utg.onePairCombo('6', 0.5)
    utg.onePairCombo('5', 0.4)
    utg.onePairCombo('4', 0.35)
    utg.onePairCombo('3', 0.2)
    utg.onePairCombo('2', 0.2)

    utg.addSuitedGivenFirstCard('A', 3, 13)
    utg.oneSuitedCombo('A', '2', 0.5)
    utg.addSuitedGivenFirstCard('K', 8, 12)
    utg.oneSuitedCombo('K', '5', 0.4)
    utg.oneSuitedCombo('K', '6', 0.35)
    utg.oneSuitedCombo('K', '7', 0.1)

    utg.addSuitedGivenFirstCard('Q', 9, 11)
    utg.addSuitedGivenFirstCard('J', 10, 10)
    utg.addSuitedGivenFirstCard('T', 9, 9)
    utg.oneSuitedCombo('8', '7', 0.3)
    utg.oneSuitedCombo('7', '6', 0.3)
    utg.oneSuitedCombo('6', '5', 0.3)
    utg.oneSuitedCombo('5', '4', 0.3)

    utg.addOffSuitGivenFirstCard('A', 10, 13)
    utg.addOffSuitGivenFirstCard('K', 11, 12)

    utg.oneOffSuitCombo('K', 'T', 0.25)
    utg.oneOffSuitCombo('Q', 'J', 0.5)

    ########
    bb.addPair(2,10)
    bb.onePairCombo('J', 0.9)

    bb.addSuitedGivenFirstCard('A', 6, 9)
    bb.oneSuitedCombo('A', '2', 0.9)
    bb.oneSuitedCombo('A', '3', 0.6)
    bb.oneSuitedCombo('A', '4', 0.5)
    bb.oneSuitedCombo('A', '5', 0.55)
    bb.oneSuitedCombo('A', 'T', 0.5)
    bb.oneSuitedCombo('A', 'J', 0.6)
    bb.oneSuitedCombo('A', 'Q', 0.3)

    bb.addSuitedGivenFirstCard('K', 2, 4)
    bb.addSuitedGivenFirstCard('K', 8, 9)
    bb.oneSuitedCombo('K', '5', 0.45)
    bb.oneSuitedCombo('K', '6', 0.5)
    bb.oneSuitedCombo('K', '7', 0.65)
    bb.oneSuitedCombo('K', 'T', 0.6)
    bb.oneSuitedCombo('K', 'J', 0.2)


    bb.addSuitedGivenFirstCard('Q', 5, 9)
    bb.oneSuitedCombo('Q', 'T', 0.6)
    bb.oneSuitedCombo('Q', 'J', 0.4)
    bb.addSuitedGivenFirstCard('J', 8, 10)
    bb.addSuitedGivenFirstCard('T', 7, 9)
    bb.addSuitedGivenFirstCard('9', 6, 7)
    bb.oneSuitedCombo('9', '8', 0.8)
    bb.addSuitedGivenFirstCard('8', 5, 6)
    bb.oneSuitedCombo('8', '7', 0.8)
    bb.addSuitedGivenFirstCard('7', 5, 5)
    bb.oneSuitedCombo('7', '5', 0.45)
    bb.oneSuitedCombo('7', '6', 0.55)
    bb.addSuitedGivenFirstCard('6', 4, 4)
    bb.oneSuitedCombo('6', '3', 0.4)
    bb.oneSuitedCombo('6', '5', 0.5)
    bb.addSuitedGivenFirstCard('5', 3, 4)
    bb.oneSuitedCombo('5', '2', 0.5)
    bb.addSuitedGivenFirstCard('4', 3, 3)
    bb.oneSuitedCombo('4', '2', 0.5)

    bb.addOffSuitGivenFirstCard('A', 10, 11)
    bb.oneOffSuitCombo('A', 'Q', 0.8)
    bb.oneOffSuitCombo('A', 'K', 0.25)
    bb.addOffSuitGivenFirstCard('K', 11, 12)
    bb.oneOffSuitCombo('Q', 'J', 0.45)

    return utg, bb