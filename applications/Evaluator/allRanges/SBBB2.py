import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def SBBB2():
    sb = r.Range()
    bb  = r.Range()

    sb.addPair(2,14)

    sb.addSuitedGivenFirstCard('A', 2, 13)
    sb.addSuitedGivenFirstCard('K', 2, 12)
    sb.addSuitedGivenFirstCard('Q', 2, 11)
    sb.addSuitedGivenFirstCard('J', 4, 10)
    sb.addSuitedGivenFirstCard('T', 6, 9)
    sb.addSuitedGivenFirstCard('9', 5, 8)
    sb.addSuitedGivenFirstCard('8', 5, 7)
    sb.addSuitedGivenFirstCard('7', 4, 6)
    sb.addSuitedGivenFirstCard('6', 4, 5)
    sb.addSuitedGivenFirstCard('5', 3, 4)

    sb.addOffSuitGivenFirstCard('A', 4, 13)
    sb.addOffSuitGivenFirstCard('K', 7, 12)
    sb.addOffSuitGivenFirstCard('Q', 9, 11)
    sb.addOffSuitGivenFirstCard('J', 9, 10)
    sb.addOffSuitGivenFirstCard('T', 8, 9)
    sb.addOffSuitGivenFirstCard('9', 8, 8)

    sb.oneOffSuitCombo('A', '3', 0.25)
    sb.oneOffSuitCombo('Q', '8', 0.5)
    sb.oneOffSuitCombo('J', '8', 0.20)
    sb.oneOffSuitCombo('8', '7', 0.5)

    #######
    bb.addPair(2,5)
    bb.onePairCombo('6', 0.6)
    bb.onePairCombo('7', 0.45)
    bb.onePairCombo('8', 0.25)

    bb.oneSuitedCombo('A', '2', 0.3)
    bb.oneSuitedCombo('A', '3', 0.3)
    bb.oneSuitedCombo('A', '6', 0.9)
    bb.oneSuitedCombo('A', '7', 0.8)
    bb.oneSuitedCombo('A', '8', 1)
    bb.oneSuitedCombo('A', '9', 0.8)

    bb.addSuitedGivenFirstCard('K', 2, 5)
    bb.oneSuitedCombo('K', '6', 0.75)
    bb.oneSuitedCombo('K', '7', 0.75)
    bb.oneSuitedCombo('K', '8', 0.4)
    bb.oneSuitedCombo('K', '9', 0.5)
    bb.addSuitedGivenFirstCard('Q', 2, 9)
    bb.oneSuitedCombo('Q', 'T', 0.3)
    bb.addSuitedGivenFirstCard('J', 2, 8)
    bb.oneSuitedCombo('J', '9', 0.4)
    bb.oneSuitedCombo('J', 'T', 0.2)
    bb.addSuitedGivenFirstCard('T', 2, 7)
    bb.oneSuitedCombo('T', '8', 0.3)
    bb.addSuitedGivenFirstCard('9', 2, 6)
    bb.oneSuitedCombo('9', '7', 0.25)
    bb.addSuitedGivenFirstCard('8', 2, 5)
    bb.oneSuitedCombo('8', '6', 0.55)
    bb.addSuitedGivenFirstCard('7', 2, 4)
    bb.oneSuitedCombo('7', '5', 0.5)
    bb.addSuitedGivenFirstCard('6', 2, 3)
    bb.oneSuitedCombo('6', '4', 0.25)
    bb.addSuitedGivenFirstCard('5', 2, 2)
    bb.oneSuitedCombo('5', '3', 0.25)
    bb.addSuitedGivenFirstCard('4', 2, 3)
    bb.addSuitedGivenFirstCard('3', 2, 2)

    bb.addOffSuitGivenFirstCard('A', 7, 10)
    bb.oneOffSuitCombo('A','J', 0.5)
    bb.oneOffSuitCombo('A', '6', 0.6)
    bb.oneOffSuitCombo('A', '4', 0.7)
    bb.oneOffSuitCombo('A', '2', 0.6)

    bb.addOffSuitGivenFirstCard('K', 9, 11)
    bb.oneOffSuitCombo('K', '2', 0.3)
    bb.oneOffSuitCombo('K', '3', 0.9)
    bb.oneOffSuitCombo('K', '4', 0.6)
    bb.oneOffSuitCombo('K', '5', 0.55)
    bb.oneOffSuitCombo('K', '6', 0.7)
    bb.oneOffSuitCombo('K', '7', 0.6)
    bb.oneOffSuitCombo('K', '8', 0.6)
    bb.oneOffSuitCombo('K', 'Q', 0.4)

    bb.addOffSuitGivenFirstCard('Q', 9, 11)
    bb.oneOffSuitCombo('Q', '5', 0.3)
    bb.oneOffSuitCombo('Q', '6', 0.6)
    bb.oneOffSuitCombo('Q', '7', 0.8)
    bb.oneOffSuitCombo('Q', '8', 0.6)
    bb.oneOffSuitCombo('Q', '9', 0.8)

    bb.oneOffSuitCombo('J', '7', 0.4)
    bb.oneOffSuitCombo('J', '8', 0.6)
    bb.oneOffSuitCombo('J', '9', 0.7)
    bb.oneOffSuitCombo('J', 'T', 1)
    bb.oneOffSuitCombo('T', '9', 1)
    bb.oneOffSuitCombo('T', '8', 0.8)
    bb.oneOffSuitCombo('T', '7', 0.6)

    bb.oneOffSuitCombo('9', '7', 0.9)
    bb.oneOffSuitCombo('9', '8', 0.8)
    bb.oneOffSuitCombo('9', '6', 0.25)
    bb.addOffSuitGivenFirstCard('8', 6, 7)
    bb.addOffSuitGivenFirstCard('7', 5, 6)

    bb.oneOffSuitCombo('6', '5', 1)
    bb.oneOffSuitCombo('6', '4', 0.75)
    bb.oneOffSuitCombo('5', '4', 1)
    bb.oneOffSuitCombo('5', '3', 1)
    bb.oneOffSuitCombo('4', '3', 0.5)

    return sb, bb



