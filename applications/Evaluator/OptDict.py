class optDict():
    def __init__(self, suits):
        # holds equity and weight, and key is [hand (card1, card2), type]
        self.opt = dict()
        self.suits = []
        for s in suits:
            self.suits.append(s[0])
        # if len is 2, first suit must be the one w bdfd
        self.length = len(self.suits)

    def isInDict(self, card1, card2, type):
        if self.length == 3: return self.checkInThree(card1, card2, type)
        elif self.length == 2: return self.checkInTwo(card1, card2, type)
        else: return self.checkInOne(card1, card2, type)
    def create(self, card1, card2, equity, type):
        # run create if no dictionary value is present, i.e. when isindict is false
        if self.length == 3: self.createSuitThree(card1, card2, equity, type)
        elif self.length == 2: self.createSuitTwo(card1, card2, equity, type)
        else: self.createSuitOne(card1, card2, equity, type)

    def retrieve(self, card1, card2, type):
        # use retrieve when isindict is true, which will return the equity and weight
        if self.length == 3: return self.getThree(card1, card2, type)
        elif self.length == 2: return self.getTwo(card1, card2, type)
        else: return self.getOne(card1, card2, type)


    # for three toned flops:
    def checkInThree(self, a, b, type):
        return True if (a.value, b.value, type) in self.opt else False

    def getThree(self, a, b, type):
        return self.opt[(a.value, b.value, type)]

    def createSuitThree(self, a, b, eq, type):
        if(type == 'p'): self.opt[(a.value, b.value, 'p')] = eq
        elif(type == 'o'):self.opt[(a.value, b.value, 'o')] = eq
        else:
            if a.suit in self.suits: self.opt[(a.value, b.value, 's')] = eq


    # for two toned flops:
    def checkInTwo(self, a, b, type):
        if (type == 'p'):
            if (a.suit == self.suits[0] or b.suit == self.suits[0]):
                return True if (a.value, b.value, 'pairS') in self.opt else False
            else: return True if (a.value, b.value, 'pairNoS') in self.opt else False
        elif(type == 'o'):
            if(a.suit == self.suits[0]): return True if (a.value, b.value, 'firstOffsuit') in self.opt else False
            elif (b.suit == self.suits[0]): return True if (a.value, b.value, 'secondOffsuit') in self.opt else False
            else: return True if (a.value, b.value, 'o') in self.opt else False
        else:
            if (a.suit != self.suits[0] and a.suit != self.suits[1]): return True if (a.value, b.value, 's') in self.opt else False
            else: return False

    def getTwo(self, a, b, type):
        if (type == 's'): return self.opt[(a.value, b.value, type)]
        elif (type == 'p'):
            if (a.suit == self.suits[0] or b.suit == self.suits[0]): return self.opt[(a.value, b.value, 'pairS')]
            else: return self.opt[(a.value, b.value, 'pairNoS')]
        else:
            if (a.suit == self.suits[0]): return self.opt[(a.value, b.value, 'firstOffsuit')]
            elif (b.suit == self.suits[0]): return self.opt[(a.value, b.value, 'secondOffsuit')]
            else: return self.opt[(a.value, b.value, 'o')]

    def createSuitTwo(self, a, b, eq, type):
        if (type == 'p'):
            if (a.suit == self.suits[0] or b.suit == self.suits[0]):
                self.opt[(a.value, b.value, 'pairS')] = eq
            else:
                self.opt[(a.value, b.value, 'pairNoS')] = eq
        elif (type == 'o'):
            if(a.suit == self.suits[0]): self.opt[(a.value, b.value, 'firstOffsuit')] = eq
            elif(b.suit == self.suits[0]): self.opt[(a.value, b.value, 'secondOffsuit')] = eq
            else: self.opt[(a.value, b.value, 'o')] = eq
        else:
            if (a.suit != self.suits[0] and a.suit != self.suits[1]): self.opt[(a.value, b.value, 's')] = eq


    # for monotone flop:
    def checkInOne(self, a, b, type):
        if (type == 'p'):
            if (a.suit == self.suits[0] or b.suit == self.suits[0]):
                return True if (a.value, b.value, 'pairS') in self.opt else False
            else: return True if (a.value, b.value, 'pairNoS') in self.opt else False
        elif type == 'o':
            if (a.suit == self.suits[0]): return True if (a.value, b.value, 'firstOffsuit') in self.opt else False
            elif (b.suit == self.suits[0]): return True if (a.value, b.value, 'secondOffsuit') in self.opt else False
            else: return True if (a.value, b.value, 'o') in self.opt else False
        else:
            if (a.suit != self.suits[0]): return True if (a.value, b.value, 's') in self.opt else False
            else: return False

    def getOne(self, a, b, type):
        if (type == 'p'):
            if (a.suit == self.suits[0] or b.suit == self.suits[0]): return self.opt[(a.value, b.value, 'pairS')]
            else: return self.opt[(a.value, b.value, 'pairNoS')]
        elif (type == 'o'):
            if(a.suit == self.suits[0]): return self.opt[(a.value, b.value, 'firstOffsuit')]
            elif (b.suit == self.suits[0]): return self.opt[(a.value, b.value, 'secondOffsuit')]
            else: return self.opt[(a.value, b.value, 'o')]
        else:
            return self.opt[(a.value, b.value, 's')]

    def createSuitOne(self, a, b, eq, type):
        if (type == 'p'):
            if(a.suit == self.suits[0] or b.suit == self.suits[0]): self.opt[(a.value, b.value, 'pairS')] = eq
            else: self.opt[(a.value, b.value, 'pairNoS')] = eq
        elif (type == 'o'):
            if (a.suit == self.suits[0]): self.opt[(a.value, b.value, 'firstOffsuit')] = eq
            elif (b.suit == self.suits[0]): self.opt[(a.value, b.value, 'secondOffsuit')] = eq
            else: self.opt[(a.value, b.value, 'o')] = eq
        else:
            if (a.suit != self.suits[0]): self.opt[(a.value, b.value, 's')] = eq




