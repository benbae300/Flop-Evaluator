from . import card as c

class Range():
    def __init__(self):
        # [card1, card2, weight]
        self.range = list()
        self.suit = ['h', 'c','d', 's']
        self.value = {2:'2', 3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',
                          9:'9',10:'T',11:'J',12:'Q',13:'K',14:'A',}
    def returnRange(self):
        return self.range

    def oneSuitedCombo(self, firstCard, secondCard, weight):
        # adds one suited combo of specfic weight
        for s in self.suit:
            self.range.append([c.Card(firstCard, s), c.Card(secondCard, s), weight, 's'])

    def oneOffSuitCombo(self, firstCard, secondCard, weight):
        # adds one suited combo of specfic weight
        for s1 in self.suit:
            for s2 in self.suit:
                if s1 != s2: self.range.append([c.Card(firstCard, s1), c.Card(secondCard, s2), weight, 'o'])

    def onePairCombo(self, pair, weight):
        # adds one pair of specific weight
        i = 0
        while (i < 4):
            j = i + 1
            while (j < 4):
                self.range.append([c.Card(pair, self.suit[i]), c.Card(pair, self.suit[j]), weight, 'p'])
                j += 1
            i += 1

    def addSuitedGivenFirstCard(self, firstCard, start, end):
        # adds offsuit combos given range and first card, assumes weight is one
        for val in range(start, end+1):
            if firstCard == self.value[val]: continue
            for s in self.suit:
                self.range.append([c.Card(firstCard, s), c.Card(self.value[val], s), 1, 's'])

    def addOffSuitGivenFirstCard(self, firstCard, start, end):
        # adds offsuit combos given range and first card, assumes weight is one
        for val in range(start, end+1):
            if firstCard == self.value[val]: continue
            for s1 in self.suit:
                for s2 in self.suit:
                    if s1 != s2: self.range.append([c.Card(firstCard, s1), c.Card(self.value[val], s2), 1, 'o'])

    def addSuitedGivenSecondCard(self, secondCard, start, end):
        # adds offsuit combos given range and second card, assumes weight is one
        for val in range(start, end+1):
            if secondCard == self.value[val]: continue
            for s in self.suit:
                self.range.append([c.Card(self.value[val], s), c.Card(secondCard, s), 1, 's'])

    def addOffSuitGivenSecondCard(self, secondCard, start, end):
        # adds offsuit combos given range and second card, assumes weight is one
        for val in range(start, end+1):
            if secondCard == self.value[val]: continue
            for s1 in self.suit:
                for s2 in self.suit:
                    if s1 != s2: self.range.append([c.Card(self.value[val], s1),  c.Card(secondCard, s2), 1, 'o'])

    def addPair(self, start, end):
        # adds a pair assuming weight is 1
        for pair in range(start, end+1):
            i = 0
            while (i < 4):
                j = i + 1
                while (j < 4):
                    self.range.append([c.Card(self.value[pair], self.suit[i]), c.Card(self.value[pair], self.suit[j]), 1, 'p'])
                    j += 1
                i += 1
