import sys
sys.path.insert(1, '../')
from applications.Evaluator import Range as r

def SBUTG3():
    sb = r.Range()
    utg  = r.Range()

    sb.addPair(11, 14)
    sb.onePairCombo('T', 0.7)
    sb.onePairCombo('9', 0.4)
    sb.onePairCombo('8', 0.2)
    sb.onePairCombo('7', 0.1)

    sb.addSuitedGivenFirstCard('A', 10, 13)
    sb.oneSuitedCombo('A', '5', 1)
    sb.oneSuitedCombo('A', '4', 0.75)
    sb.addSuitedGivenFirstCard('K', 10, 12)
    sb.oneSuitedCombo('K', '9', 0.2)
    sb.oneSuitedCombo('K', '6', 0.5)
    sb.oneSuitedCombo('Q', 'J', 0.5)
    sb.oneSuitedCombo('7', '6', 0.2)
    sb.oneSuitedCombo('6', '5', 0.3)

    sb.addOffSuitGivenFirstCard('A', 12,13)
    sb.oneOffSuitCombo('K', 'Q', 0.2)

    utg.addPair(11,12)
    utg.onePairCombo('T', 0.6)
    utg.onePairCombo('9', 0.5)
    utg.onePairCombo('8', 0.33)
    utg.onePairCombo('7', 0.33)
    utg.onePairCombo('6', 0.25)
    utg.onePairCombo('5', 0.1)
    utg.onePairCombo('4', 0.14)
    utg.onePairCombo('K', 0.25)
    utg.onePairCombo('A', 0.3)


    utg.addSuitedGivenFirstCard('A', 11,12)
    utg.oneSuitedCombo('A', 'T', 0.5)
    utg.oneSuitedCombo('A', '5', 0.55)
    utg.oneSuitedCombo('A', '4', 0.35)

    utg.addSuitedGivenFirstCard('K', 11,12)
    utg.oneSuitedCombo('K', 'T', 0.5)

    utg.oneSuitedCombo('T', '9', 0.3)
    utg.oneSuitedCombo('8', '7', 0.3)
    utg.oneSuitedCombo('7', '6', 0.3)
    utg.oneSuitedCombo('6', '5', 0.3)
    utg.oneSuitedCombo('5', '4', 0.3)

    utg.oneOffSuitCombo('A', 'K', 0.25)
    utg.oneOffSuitCombo('A', 'Q', 0.2)

    return sb, utg

