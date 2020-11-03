import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def SBBU3():
    sb = r.Range()
    bu  = r.Range()

    sb.addPair(8, 14)
    sb.onePairCombo('7', 0.35)

    sb.addSuitedGivenFirstCard('A', 7, 13)
    sb.addSuitedGivenFirstCard('K', 9, 12)
    sb.addSuitedGivenFirstCard('Q', 9, 11)
    sb.addSuitedGivenFirstCard('J', 10, 10)
    sb.oneSuitedCombo('A', '2', 0.1)
    sb.oneSuitedCombo('A', '3', 0.2)
    sb.oneSuitedCombo('A', '4', 0.8)
    sb.oneSuitedCombo('A', '5', 1)
    sb.oneSuitedCombo('A', '6', 0.65)

    sb.oneSuitedCombo('K', '6', 0.6)
    sb.oneSuitedCombo('K', '8', 0.4)

    sb.addOffSuitGivenFirstCard('A', 10, 13)
    sb.oneOffSuitCombo('K', 'T', 0.3)
    sb.oneOffSuitCombo('K', 'J', 0.65)
    sb.oneOffSuitCombo('K', 'Q', 1)

    bu.addSuitedGivenFirstCard('A', 10, 11)
    bu.oneSuitedCombo('A', 'Q', 0.55)
    bu.oneSuitedCombo('A', '9', 0.4)
    bu.oneSuitedCombo('A', '8', 0.3)
    bu.oneSuitedCombo('A', '5', 0.4)
    bu.oneSuitedCombo('A', '4', 0.2)
    bu.oneSuitedCombo('A', '3', 0.2)
    bu.addSuitedGivenFirstCard('K', 10, 12)
    bu.oneSuitedCombo('K', '9', 0.4)
    bu.oneSuitedCombo('Q', 'J', 1)
    bu.oneSuitedCombo('Q', 'T', 0.6)
    bu.oneSuitedCombo('J', 'T', 0.6)
    bu.oneSuitedCombo('T', '9', 0.5)
    bu.oneSuitedCombo('T', '8', 0.2)

    bu.oneSuitedCombo('9', '8', 0.2)
    bu.oneSuitedCombo('8', '7', 0.2)
    bu.oneSuitedCombo('6', '5', 0.2)
    bu.oneSuitedCombo('5', '4', 0.5)

    bu.oneOffSuitCombo('A', 'J', 0.3)
    bu.oneOffSuitCombo('A', 'Q', 0.3)
    bu.oneOffSuitCombo('K', 'Q', 0.3)

    bu.onePairCombo('4', 0.3)
    bu.onePairCombo('5', 0.4)
    bu.onePairCombo('6', 0.4)
    bu.onePairCombo('7', 0.65)
    bu.onePairCombo('8', 0.9)
    bu.onePairCombo('9', 0.5)
    bu.onePairCombo('A', 0.8)

    return sb, bu

