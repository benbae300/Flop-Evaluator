import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def COBU4():
    co = r.Range()
    bu = r.Range()

    co.addPair(11, 14)
    co.onePairCombo('T', 0.6)
    co.onePairCombo('9', 0.15)
    co.addSuitedGivenFirstCard('A', 13, 13)
    co.oneSuitedCombo('A', '4', 0.45)
    co.oneSuitedCombo('A', '5', 0.5)
    co.oneSuitedCombo('A', '8', 0.3)
    co.oneSuitedCombo('A', '9', 0.3)
    co.oneSuitedCombo('A', 'T', 0.5)
    co.oneSuitedCombo('A', 'J', 0.2)
    co.oneSuitedCombo('A', 'Q', 0.3)

    co.oneOffSuitCombo('A', 'J', 0.15)
    co.oneOffSuitCombo('A', 'Q', 0.75)
    co.oneOffSuitCombo('A', 'K', 1)

    co.oneSuitedCombo('K', 'J', 1)
    co.oneSuitedCombo('K', 'T', 0.7)
    co.oneSuitedCombo('K', 'Q', 0.7)
    co.oneSuitedCombo('Q', 'T', 0.1)
    co.oneSuitedCombo('Q', 'J', 0.4)
    co.oneSuitedCombo('J', 'T', 0.4)

    co.oneSuitedCombo('K', '9', 0.35)
    co.oneSuitedCombo('T', '9', 0.3)

    bu.onePairCombo('A', 1)
    bu.onePairCombo('K', 0.3)
    bu.onePairCombo('Q', 0.5)
    bu.addPair(9, 11)
    bu.onePairCombo('6', 0.5)
    bu.onePairCombo('7', 0.7)
    bu.onePairCombo('8', 0.7)

    bu.oneSuitedCombo('A', '3', 0.2)
    bu.oneSuitedCombo('A', '9', 0.2)
    bu.oneSuitedCombo('K', '9', 0.5)
    bu.addSuitedGivenFirstCard('A', 4, 5)
    bu.oneSuitedCombo('8', '7', 0.2)
    bu.oneSuitedCombo('7', '6', 0.2)
    bu.oneSuitedCombo('6', '5', 0.1)
    bu.oneSuitedCombo('5', '4', 0.3)
    bu.oneSuitedCombo('A', 'T', 0.7)
    bu.addSuitedGivenFirstCard('A', 11, 13)
    bu.addSuitedGivenFirstCard('K', 10, 12)
    bu.oneSuitedCombo('K', '6', 0.3)
    bu.oneOffSuitCombo('A', 'Q', 1)

    return co, bu