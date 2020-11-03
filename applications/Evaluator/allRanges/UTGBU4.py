import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def UTGBU4():
    utg = r.Range()
    bu  = r.Range()

    utg.addPair(13,14)
    utg.onePairCombo('9', 0.2)
    utg.onePairCombo('T', 0.2)
    utg.onePairCombo('J', 0.4)
    utg.onePairCombo('Q', 0.65)

    utg.oneSuitedCombo('A', 'K', 1)
    utg.oneSuitedCombo('A', 'Q', 0.1)
    utg.oneSuitedCombo('A', 'J', 0.5)
    utg.oneSuitedCombo('A', 'T', 0.4)
    utg.oneSuitedCombo('A', '5', 0.5)
    utg.oneSuitedCombo('A', '4', 0.3)
    utg.oneSuitedCombo('K', 'Q', 0.5)
    utg.oneSuitedCombo('K', 'J', 0.4)
    utg.oneSuitedCombo('K', 'T', 0.4)
    utg.oneSuitedCombo('Q', 'J', 0.1)
    utg.oneSuitedCombo('J', 'T', 0.1)

    utg.oneOffSuitCombo('A', 'Q', 0.25)
    utg.oneOffSuitCombo('A', 'K', 0.8)

    ######
    bu.onePairCombo('A', 1)
    bu.onePairCombo('Q', 0.9)
    bu.onePairCombo('J', 0.3)
    bu.onePairCombo('T', 0.25)
    bu.onePairCombo('9', 0.25)
    bu.onePairCombo('8', 0.25)
    bu.onePairCombo('7', 0.25)
    bu.onePairCombo('6', 0.2)
    bu.oneSuitedCombo('A','5', 0.3)
    bu.oneSuitedCombo('A','4', 0.35)
    bu.oneSuitedCombo('A','Q', 0.85)

    bu.oneSuitedCombo('A', 'K', 0.2)

    bu.oneSuitedCombo('8','7', 0.3)
    bu.oneSuitedCombo('7','6', 0.2)
    bu.oneSuitedCombo('6','5', 0.3)
    bu.oneSuitedCombo('5','4', 0.3)
    bu.oneSuitedCombo('J','T', 0.25)
    bu.oneSuitedCombo('T','9', 0.25)

    bu.oneOffSuitCombo('A', 'K', 0.25)

    return utg, bu