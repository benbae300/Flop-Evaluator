import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def SBCO3():
    sb = r.Range()
    co = r.Range()

    sb.addPair(9, 14)
    sb.addOffSuitGivenFirstCard('A', 11, 14)

    sb.addSuitedGivenFirstCard('K', 10, 12)
    sb.addSuitedGivenFirstCard('Q', 10, 11)
    sb.addSuitedGivenFirstCard('A', 10, 14)

    sb.oneOffSuitCombo('K', 'J', 0.5)
    sb.oneOffSuitCombo('K', 'Q', 0.9)

    sb.oneSuitedCombo('A', '9', 0.8)
    sb.oneSuitedCombo('K', '9', 0.5)
    sb.oneSuitedCombo('J', 'T', 1)
    sb.oneSuitedCombo('J', '9', 0.4)
    sb.oneSuitedCombo('T', '9', 0.4)
    sb.oneSuitedCombo('A', '5', 1)
    sb.oneSuitedCombo('A', '4', 0.8)
    sb.oneSuitedCombo('K', '6', 0.4)

    sb.onePairCombo('8', 0.5)
    sb.onePairCombo('7', 0.2)
    sb.onePairCombo('6', 0.15)

    ########
    co.addPair(9, 10)

    co.addSuitedGivenFirstCard('K', 10, 12)
    co.addSuitedGivenFirstCard('A', 10, 12)

    co.oneSuitedCombo('A', 'K', 0.3)
    co.oneSuitedCombo('Q', 'J', 0.8)
    co.oneSuitedCombo('Q', 'T', 0.5)
    co.oneSuitedCombo('J', 'T', 1)
    co.oneSuitedCombo('T', '9', 0.6)
    co.oneSuitedCombo('A', '5', 0.7)
    co.oneSuitedCombo('A', '4', 0.4)
    co.oneSuitedCombo('8', '7', 0.4)
    co.oneSuitedCombo('7', '6', 0.5)
    co.oneSuitedCombo('6', '5', 0.2)
    co.oneSuitedCombo('5', '4', 0.5)

    co.oneOffSuitCombo('A', 'Q', 0.8)

    co.onePairCombo('J',0.35)
    co.onePairCombo('8',0.5)
    co.onePairCombo('7', 0.5)
    co.onePairCombo('6', 0.5)
    co.onePairCombo('5', 0.1)
    co.onePairCombo('4', 0.1)
    co.onePairCombo('A', 0.7)
    return sb, co

