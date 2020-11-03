import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def UTGBU2():
    utg = r.Range()
    bu  = r.Range()

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
    #######
    bu.oneSuitedCombo('A','Q', 0.15)
    bu.oneSuitedCombo('A','J', 0.5)
    bu.oneSuitedCombo('A','T', 0.45)
    bu.oneSuitedCombo('A','9', 0.2)
    bu.oneSuitedCombo('A','5', 0.35)
    bu.oneSuitedCombo('A','4', 0.3)
    bu.oneSuitedCombo('A','8', 0.1)
    bu.oneSuitedCombo('A','7', 0.1)


    bu.oneSuitedCombo('K','Q', 0.3)
    bu.oneSuitedCombo('K','J', 0.45)
    bu.oneSuitedCombo('K','T', 0.3)
    bu.oneSuitedCombo('Q','J', 0.2)
    bu.oneSuitedCombo('Q','T', 0.25)
    bu.oneSuitedCombo('J','T', 0.4)
    bu.oneSuitedCombo('T','9', 0.4)
    bu.oneSuitedCombo('8','7', 0.2)
    bu.oneSuitedCombo('7','6', 0.2)
    bu.oneSuitedCombo('6','5', 0.2)
    bu.oneSuitedCombo('5','4', 0.2)

    bu.oneOffSuitCombo('A','K',0.25)
    bu.oneOffSuitCombo('A','Q',0.45)
    bu.oneOffSuitCombo('K','Q',0.1)

    bu.onePairCombo('Q', 0.1)
    bu.onePairCombo('J', 0.4)
    bu.onePairCombo('T', 0.4)
    bu.onePairCombo('9', 0.5)
    bu.onePairCombo('8', 0.5)
    bu.onePairCombo('7', 0.5)
    bu.onePairCombo('6', 0.3)
    bu.onePairCombo('5', 0.25)
    bu.onePairCombo('4', 0.2)
    bu.onePairCombo('3', 0.2)
    bu.onePairCombo('2', 0.25)



    return utg, bu 