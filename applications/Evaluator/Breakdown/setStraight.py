def setStraight(flopVal):
    curFlop = flopVal[:]
    straightCards = []
    curFlop.sort()
    if 14 in curFlop and curFlop[2] - curFlop[0] > 4:
        curFlop.remove(14)
        curFlop.insert(0, 1)

    maxFlop = curFlop[2]
    minFlop = curFlop[0]
    if curFlop[2] - curFlop[0] == 2:
        if maxFlop == 14:
            straightCards.append(11)
            straightCards.append(10)
        elif maxFlop == 13:
            straightCards.append(14)
            straightCards.append(10)
            straightCards.append(9)
        elif minFlop == 1:
            straightCards.append(4)
            straightCards.append(5)
        elif minFlop == 2:
            straightCards.append(14)
            straightCards.append(5)
            straightCards.append(6)
        elif minFlop == 3:
            straightCards.append(14)
            straightCards.append(6)
            straightCards.append(7)
        else:
            straightCards.append(maxFlop + 1)
            straightCards.append(maxFlop + 2)
            straightCards.append(minFlop - 1)
    elif curFlop[2] - curFlop[0] == 3:
        if maxFlop == 14:
            for i in range(10, 15):
                if i not in curFlop:
                    straightCards.append(i)
        else:
            for i in range(minFlop, maxFlop + 2):
                if i not in curFlop:
                    straightCards.append(i)

    else:
        for i in range(curFlop[0], curFlop[2] + 1):
            if i not in curFlop:
                straightCards.append(i)
    return straightCards