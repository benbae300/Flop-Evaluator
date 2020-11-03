import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def HJUTG3():
    hj = r.Range()
    utg  = r.Range()

    hj.addPair(10,14)
    hj.onePairCombo('9', 0.8)
    hj.onePairCombo('8', 0.25)

    hj.addSuitedGivenFirstCard('A', 10, 13)
    hj.addSuitedGivenFirstCard('K', 10, 12)
    hj.addSuitedGivenFirstCard('Q', 11, 11)
    hj.oneSuitedCombo('A', '9', 0.3)
    hj.oneSuitedCombo('A', '8', 0.4)
    hj.oneSuitedCombo('A', '7', 0.2)
    hj.oneSuitedCombo('A', '5', 1)
    hj.oneSuitedCombo('A', '4', 0.5)
    hj.oneSuitedCombo('K', '9', 0.35)

    hj.oneSuitedCombo('8', '7', 0.1)
    hj.oneSuitedCombo('7', '6', 0.15)
    hj.oneSuitedCombo('6', '5', 0.2)
    hj.oneSuitedCombo('5', '4', 0.15)

    hj.oneOffSuitCombo('A','Q',0.8)
    hj.oneOffSuitCombo('A','K',1)
    hj.oneOffSuitCombo('K','Q',0.2)
    ########

    utg.onePairCombo('Q', 0.3)
    utg.onePairCombo('J', 0.6)
    utg.onePairCombo('T', 0.75)
    utg.onePairCombo('9', 0.7)
    utg.onePairCombo('8', 0.5)
    utg.onePairCombo('7', 0.5)
    utg.onePairCombo('6', 0.5)
    utg.onePairCombo('5', 0.4)
    utg.onePairCombo('4', 0.35)
    utg.onePairCombo('3', 0.2)
    utg.onePairCombo('2', 0.2)

    utg.oneSuitedCombo('A', 'Q', 0.9)
    utg.oneSuitedCombo('A', 'J', 0.55)
    utg.oneSuitedCombo('A', 'T', 0.4)
    utg.oneSuitedCombo('A', '5', 0.5)
    utg.oneSuitedCombo('A', '4', 0.25)
    utg.oneSuitedCombo('K', 'Q', 0.5)
    utg.oneSuitedCombo('K', 'J', 0.6)
    utg.oneSuitedCombo('K', 'T', 0.4)

    utg.oneSuitedCombo('T', '9', 0.5)
    utg.oneSuitedCombo('8', '7', 0.3)
    utg.oneSuitedCombo('7', '6', 0.3)
    utg.oneSuitedCombo('6', '5', 0.3)
    utg.oneSuitedCombo('5', '4', 0.3)



    return hj, utg
