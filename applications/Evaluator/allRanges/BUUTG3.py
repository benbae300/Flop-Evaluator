import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def BUUTG3():
    utg = r.Range()
    bu  = r.Range()

    bu.addPair(13,14)
    bu.oneSuitedCombo('A', 'K', 1)
    bu.oneSuitedCombo('A','Q', 0.85)
    bu.oneSuitedCombo('A','J', 0.5)
    bu.oneSuitedCombo('A','T', 0.55)
    bu.oneSuitedCombo('A','9', 0.8)
    bu.oneSuitedCombo('A','5', 0.65)
    bu.oneSuitedCombo('A','4', 0.7)

    bu.oneSuitedCombo('A','8', 0.6)
    bu.oneSuitedCombo('A','7', 0.3)

    bu.oneSuitedCombo('K','Q', 0.7)
    bu.oneSuitedCombo('K','J', 0.55)
    bu.oneSuitedCombo('K','T', 0.7)
    bu.oneSuitedCombo('K','9', 0.7)
    bu.oneSuitedCombo('Q','J', 0.8)
    bu.oneSuitedCombo('Q','T', 0.75)
    bu.oneSuitedCombo('J','T', 0.6)
    bu.oneSuitedCombo('T','9', 0.5)
    bu.oneSuitedCombo('8','7', 0.3)
    bu.oneSuitedCombo('7','6', 0.2)
    bu.oneSuitedCombo('6','5', 0.3)
    bu.oneSuitedCombo('5','4', 0.3)

    bu.oneOffSuitCombo('A','K',0.75)
    bu.oneOffSuitCombo('A','Q',0.55)
    bu.oneOffSuitCombo('A','J',0.2)
    bu.oneOffSuitCombo('K','Q',0.4)

    bu.onePairCombo('Q', 0.9)
    bu.onePairCombo('J', 0.6)
    bu.onePairCombo('T', 0.6)
    bu.onePairCombo('9', 0.5)
    bu.onePairCombo('8', 0.5)
    bu.onePairCombo('7', 0.5)
    bu.onePairCombo('6', 0.2)

    ######
    utg.onePairCombo('6', 0.5)
    utg.onePairCombo('5', 0.4)
    utg.onePairCombo('4', 0.35)
    utg.onePairCombo('3', 0.2)
    utg.onePairCombo('2', 0.2)
    utg.oneSuitedCombo('8', '7', 0.3)
    utg.oneSuitedCombo('7', '6', 0.3)
    utg.oneSuitedCombo('6', '5', 0.3)
    utg.oneSuitedCombo('5', '4', 0.3)

    utg.onePairCombo('7', 0.6)
    utg.onePairCombo('8', 0.8)
    utg.onePairCombo('9', 0.8)
    utg.onePairCombo('T', 0.8)
    utg.onePairCombo('J', 0.6)
    utg.onePairCombo('Q', 0.35)

    utg.oneSuitedCombo('A', 'Q', 0.9)
    utg.oneSuitedCombo('A', 'J', 0.5)
    utg.oneSuitedCombo('A', 'T', 0.6)
    utg.oneSuitedCombo('A', '9', 0.4)
    utg.oneSuitedCombo('A', '5', 0.5)
    utg.oneSuitedCombo('A', '4', 0.4)

    utg.oneSuitedCombo('K', 'Q', 0.5)
    utg.oneSuitedCombo('K', 'J', 0.6)
    utg.oneSuitedCombo('K', 'T', 0.6)

    utg.oneSuitedCombo('J', 'T', 0.5)
    utg.oneSuitedCombo('Q', 'T', 0.4)
    utg.oneSuitedCombo('Q', 'J', 0.4)
    utg.oneSuitedCombo('T', '9', 0.5)

    utg.oneOffSuitCombo('A', 'Q', 0.1)
    utg.oneOffSuitCombo('A', 'K', 0.2)




    return bu ,utg 