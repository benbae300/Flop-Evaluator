import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def UTGCO4():
    co = r.Range()
    utg  = r.Range()

    utg.addPair(13,14)
    utg.onePairCombo('Q', 0.7)
    utg.onePairCombo('J', 0.4)
    utg.onePairCombo('T', 0.35)
    utg.onePairCombo('9', 0.1)

    utg.oneSuitedCombo('A', 'K', 1)
    utg.oneSuitedCombo('A', 'Q', 0.15)
    utg.oneSuitedCombo('A', 'J', 0.5)
    utg.oneSuitedCombo('A', 'T', 0.2)
    utg.oneSuitedCombo('A', '5', 0.5)
    utg.oneSuitedCombo('A', '4', 0.33)

    utg.oneOffSuitCombo('A', 'K', 1)
    utg.oneOffSuitCombo('A', 'Q', 0.25)
    utg.oneSuitedCombo('K', 'Q', 0.6)
    utg.oneSuitedCombo('K', 'J', 0.4)
    utg.oneSuitedCombo('K', 'T', 0.4)
    utg.oneSuitedCombo('Q', 'J', 0.1)
    ########

    co.onePairCombo('A', 0.9)
    co.oneSuitedCombo('A', 'K', 0.5)
    co.addSuitedGivenFirstCard('A', 11, 12)
    co.oneSuitedCombo('A', 'T', 0.75)
    co.oneSuitedCombo('A', '5', 0.5)
    co.oneSuitedCombo('A', '4', 0.3)
    co.oneSuitedCombo('K', 'Q', 1)
    co.oneSuitedCombo('K', 'J', 0.5)

    co.oneSuitedCombo('J', 'T', 0.5)
    co.oneSuitedCombo('8', '7', 0.1)
    co.oneSuitedCombo('7', '6', 0.15)
    co.oneSuitedCombo('6', '5', 0.2)
    co.oneSuitedCombo('5', '4', 0.1)

    co.oneOffSuitCombo('A', 'K', 0.4)

    co.onePairCombo('Q', 1)
    co.onePairCombo('J', 1)
    co.onePairCombo('T', 0.4)
    co.onePairCombo('9', 0.3)
    co.onePairCombo('8', 0.65)
    co.onePairCombo('7', 0.4)
    co.onePairCombo('6', 0.3)



    return utg, co 