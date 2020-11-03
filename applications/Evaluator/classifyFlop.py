
# figure out which type of flop it is
# then, grab what you need (pair values, straight draws, etc etc)

def classify(flop):
    tone = set()
    values = []
    isStraight = False
    for c in flop:
        values.append(c.getValue())
        tone.add(c.suit)
    if len(tone) == 1:
        return 5
    values.sort()
    if len(set(values)) == 3:
        if (values[2] - values[0]) < 5: isStraight = True
        else:
            if values[2] == 14:
                temp = values[:]
                temp.remove(14)
                temp.insert(0,1)
                if (temp[2] - temp[0]) < 5: isStraight = True

    #check for ace high straights
    if isStraight:
        if len(tone) == 3: return 1
        if len(tone) == 2: return 2
    if len(set(values)) == 3:
        if(len(tone)) == 3: return 3
        else: return 4
    elif len(set(values)) == 2:
        if len(tone) == 3: return 6
        else: return 7
    else:
        return 8

    # 1- 3 toned connected
    # 2- 2 toned connected
    # 3- 3 toned disconnected
    # 4- 2 toned disconnected
    # 5- monotone
    # 6- 3 toned paired
    # 7- 2 toned paired
    # 8- 3 same card
