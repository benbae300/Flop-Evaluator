from . import findWinner as w 
from . import Deck as d 
from . import Range as r 
from . import OptDict as o 
# some optimization factor: Take away the cards that are in hero's two cards/villians two cards/ flop when calculating
# divide flops into no fd (where all off suit combos are worth the same, and 3 of four suited combo worth same), and with fd

def findEquity(Hero, Villian, flop):
    # can probably be more efficient
    deck = d.Deck()
    heroWin, villianWin = 0, 0
    for card in flop:
        deck.remove(card)
    for card in Hero:
        deck.remove(card)
    for card in Villian:
        deck.remove(card)
    finalDeck = deck.getDeck()
    heroBoard, villianBoard = flop[:], flop[:]
    for h in Hero: heroBoard.append(h)
    for v in Villian: villianBoard.append(v)
    # use INDEXING here
    for i in range(0,45):
        for j in range(i+1, 45):
            turn, river = finalDeck[i], finalDeck[j]
            heroBoard.append(turn)
            heroBoard.append(river)
            villianBoard.append(turn)
            villianBoard.append(river)
            winner = w.findWinner(heroBoard[:],villianBoard[:])
            if winner == 1: heroWin += 1
            if winner == 2: villianWin += 1
            heroBoard.pop()
            heroBoard.pop()
            villianBoard.pop()
            villianBoard.pop()
    if heroWin == 0 and villianWin == 0: return 0
    return heroWin/(heroWin +villianWin)


def skip(flop, first, second):
    for c in flop:
        if c.equalTo(first) or c.equalTo(second): return True
    return False

def sortSuits(flop):
    suits = {'c': 0, 'd': 0, 'h': 0, 's': 0}
    reverse = {}
    for card in flop:
        suits[card.suit] += 1
    for key, value in suits.items():
        reverse.setdefault(value, list()).append(key)
    if 3 in reverse: return [reverse[3]]
    elif 2 in reverse: return [reverse[2], reverse[1]]
    else: return [s for s in reverse[1]]


def getEV(Hero, Villian, flop):
    flopSuits = sortSuits(flop)
    #heroOpt = optDict(flopSuits)
    heroTotalEquity, heroTotalWeight = 0, 0
    for combo in Hero:
        heroFirst, heroSecond, heroWeight, heroType = combo
        if skip(flop, heroFirst, heroSecond): continue
        # and here, we can skip the entire for loop
        # if in dict, we return equity, and we already know weight
        '''
        if(heroOpt.isInDict(heroFirst, heroSecond, heroType)):
            eq= heroOpt.retrieve(heroFirst, heroSecond, heroType)
            heroTotalEquity += heroWeight * eq
            heroTotalWeight += heroWeight
            continue
        '''
        heroCards = [heroFirst,heroSecond]
        heroCurrentEquity, villainTotalWeight = 0, 0
        villianOpt = o.optDict(flopSuits)
        for combo in Villian:
            villianFirst, villianSecond, villianWeight, villianType = combo
            if (heroFirst.equalTo(villianFirst) or heroFirst.equalTo(villianSecond) or heroSecond.equalTo(villianFirst) or
            heroSecond.equalTo(villianSecond)): continue
            if skip(flop, villianFirst, villianSecond): continue
            # optimize here, if already in dict quickly calculate heroCE and villianTW
            # keep track of equity -- basically we skip the findEquity function
            
            if villianOpt.isInDict(villianFirst, villianSecond, villianType):
                eq = villianOpt.retrieve(villianFirst, villianSecond, villianType)
                heroCurrentEquity += villianWeight * eq
                villainTotalWeight += villianWeight
                continue
            villianCards = [villianFirst,villianSecond]
            equity = findEquity(heroCards, villianCards, flop)
            # create new dict here, pushing in equity and villianweight
            villianOpt.create(villianFirst, villianSecond, equity, villianType)
            heroCurrentEquity += villianWeight*equity
            villainTotalWeight += villianWeight
        heroCurrentEquity /= villainTotalWeight
        # create a new dict here, as it means that it wasnt previously noted
        # we want to push in equity (herocurrenteq)
        #heroOpt.create(heroFirst, heroSecond, heroCurrentEquity, heroType)
        heroTotalEquity += heroWeight*heroCurrentEquity
        heroTotalWeight += heroWeight
    return heroTotalEquity/heroTotalWeight

def RangeAnalyzer(Hero, Villian, flop):
    heroEV = getEV(Hero, Villian.returnRange(), flop)
    return heroEV


