import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def SBBB4():
    sb = r.Range()
    bb  = r.Range()

    sb.onePairCombo('9', 0.25)
    sb.addPair(10, 14)

    sb.addSuitedGivenFirstCard('A', 12, 13)
    sb.oneSuitedCombo('A', '2', 0.1)
    sb.oneSuitedCombo('A', '3', 0.2)
    sb.oneSuitedCombo('A', '4', 0.2)
    sb.oneSuitedCombo('A', '5', 0.4)
    sb.oneSuitedCombo('A', 'T', 0.75)
    sb.oneSuitedCombo('A', 'J', 0.75)

    sb.oneSuitedCombo('K', 'T', 0.8)
    sb.oneSuitedCombo('K', 'J', 0.8)
    sb.oneSuitedCombo('K', 'Q', 0.7)

    sb.oneSuitedCombo('Q', 'T', 0.45)
    sb.oneSuitedCombo('Q', 'J', 1)

    sb.oneSuitedCombo('J', '8', 0.25)
    sb.oneSuitedCombo('J', '9', 0.2)
    sb.oneSuitedCombo('J', 'T', 0.5)

    sb.oneSuitedCombo('T', '9', 0.4)
    sb.oneSuitedCombo('T', '8', 0.4)
    sb.oneSuitedCombo('9', '8', 0.2)
    sb.oneSuitedCombo('9', '7', 0.2)
    sb.oneSuitedCombo('8', '7', 0.25)

    sb.oneSuitedCombo('7', '6', 0.35)
    sb.oneSuitedCombo('6', '5', 0.25)
    sb.oneSuitedCombo('5', '4', 0.25)

    sb.oneOffSuitCombo('A', 'T', 0.25)
    sb.oneOffSuitCombo('A', 'J', 0.5)
    sb.oneOffSuitCombo('A', 'Q', 0.7)
    sb.oneOffSuitCombo('K', 'Q', 0.25)
    sb.oneOffSuitCombo('K', 'J', 0.25)

    bb.addSuitedGivenFirstCard('A', 10, 13)
    bb.oneSuitedCombo('A', '2', 0.7)
    bb.oneSuitedCombo('A', '3', 0.7)
    bb.oneSuitedCombo('A', '6', 0.1)
    bb.oneSuitedCombo('A', '7', 0.1)
    bb.oneSuitedCombo('A', '9', 0.2)
    bb.addSuitedGivenFirstCard('K', 10, 12)
    bb.oneSuitedCombo('K', '6', 0.25)
    bb.oneSuitedCombo('K', '7', 0.25)
    bb.oneSuitedCombo('K', '8', 0.6)
    bb.oneSuitedCombo('K', '9', 0.5)
    bb.oneSuitedCombo('Q', 'T', 0.7)
    bb.oneSuitedCombo('J', '9', 0.6)
    bb.oneSuitedCombo('J', 'T', 0.8)
    bb.oneSuitedCombo('T', '8', 0.7)
    bb.oneSuitedCombo('9', '7', 0.75)
    bb.oneSuitedCombo('8', '6', 0.45)
    bb.oneSuitedCombo('7', '5', 0.5)
    bb.oneSuitedCombo('6', '4', 0.75)
    bb.oneSuitedCombo('5', '3', 0.75)
    bb.oneSuitedCombo('5', '4', 1)
    bb.oneSuitedCombo('6', '5', 1)
    bb.oneSuitedCombo('7', '6', 1)
    bb.oneSuitedCombo('8', '7', 1)
    bb.oneSuitedCombo('9', '8', 1)
    bb.oneSuitedCombo('T', '9', 1)

    bb.oneOffSuitCombo('A', 'J', 0.5)
    bb.oneOffSuitCombo('A', 'Q', 1)
    bb.oneOffSuitCombo('K', 'Q', 0.6)

    bb.onePairCombo('6', 0.4)
    bb.onePairCombo('7', 0.55)
    bb.onePairCombo('8', 0.75)
    bb.onePairCombo('9', 0.7)
    bb.onePairCombo('T', 0.6)
    bb.onePairCombo('J', 0.5)
    bb.onePairCombo('Q', 0.6)
    bb.onePairCombo('K', 0.5)
    bb.onePairCombo('A', 1)

    return sb, bb




