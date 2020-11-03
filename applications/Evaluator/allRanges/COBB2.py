import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r
def COBB2():
    co = r.Range()
    bb = r.Range()
    co.addPair(4, 14)

    co.addSuitedGivenFirstCard('A', 2, 13)
    co.addSuitedGivenFirstCard('K', 3, 12)
    co.addSuitedGivenFirstCard('Q', 6, 11)
    co.addSuitedGivenFirstCard('J', 8, 10)
    co.addSuitedGivenFirstCard('T', 8, 9)
    co.addSuitedGivenFirstCard('9', 7, 8)

    co.addOffSuitGivenFirstCard('A', 8, 13)
    co.addOffSuitGivenFirstCard('K', 10, 12)
    co.addOffSuitGivenFirstCard('Q', 10, 11)
    co.addOffSuitGivenFirstCard('J', 10, 10)

    co.oneSuitedCombo('J', '7', 0.5)
    co.oneSuitedCombo('8', '7', 0.5)
    co.oneSuitedCombo('7', '6', 0.45)
    co.oneSuitedCombo('6', '5', 0.2)
    co.oneSuitedCombo('5', '4', 0.5)

    co.oneOffSuitCombo('A', '5', 0.5)
    co.oneOffSuitCombo('K', '9', 0.5)

    co.onePairCombo('3',0.7)
    co.onePairCombo('2', 0.7)

    ###########

    bb.addPair(2, 9)
    bb.onePairCombo('T', 0.35)

    bb.addSuitedGivenFirstCard('A', 6, 11)
    bb.addSuitedGivenFirstCard('K', 2, 9)
    bb.addSuitedGivenFirstCard('Q', 3, 9)
    bb.addSuitedGivenFirstCard('J', 6, 8)
    bb.addSuitedGivenFirstCard('T', 7, 8)
    bb.addSuitedGivenFirstCard('9', 6, 7)
    bb.addSuitedGivenFirstCard('8', 5, 7)
    bb.addSuitedGivenFirstCard('7', 4, 5)
    bb.addSuitedGivenFirstCard('6', 3, 4)
    bb.addSuitedGivenFirstCard('5', 2, 4)
    bb.addSuitedGivenFirstCard('4', 3, 3)

    bb.oneSuitedCombo('A', '2', 0.8)
    bb.oneSuitedCombo('A', '3', 0.6)
    bb.oneSuitedCombo('A', '4', 0.5)
    bb.oneSuitedCombo('A', '5', 0.5)
    bb.oneSuitedCombo('A', 'Q', 0.9)
    bb.oneSuitedCombo('K', 'T', 0.2)
    bb.oneSuitedCombo('K', 'Q', 0.7)
    bb.oneSuitedCombo('Q', 'T', 0.1)
    bb.oneSuitedCombo('J', '9', 0.4)
    bb.oneSuitedCombo('T', '9', 0.4)
    bb.oneSuitedCombo('7', '6', 0.8)
    bb.oneSuitedCombo('6', '5', 0.6)

    bb.oneSuitedCombo('4', '2', 0.4)
    bb.oneSuitedCombo('5', '2', 0.6)
    bb.oneSuitedCombo('6', '3', 0.5)

    bb.addOffSuitGivenFirstCard('A', 9, 10)
    bb.addOffSuitGivenFirstCard('K', 10, 10)
    bb.addOffSuitGivenFirstCard('Q', 10, 11)
    bb.addOffSuitGivenFirstCard('J', 10, 10)

    bb.oneOffSuitCombo('A', '8', 0.65)
    bb.oneOffSuitCombo('A', '5', 0.5)

    bb.oneOffSuitCombo('A', 'J', 0.5)
    bb.oneOffSuitCombo('A', 'Q', 0.4)
    bb.oneOffSuitCombo('K', 'J', 0.7)
    bb.oneOffSuitCombo('K', 'Q', 0.8)
    
    bb.oneOffSuitCombo('J', '9', 0.4)
    bb.oneOffSuitCombo('T', '9', 0.4)

    

    return co, bb
