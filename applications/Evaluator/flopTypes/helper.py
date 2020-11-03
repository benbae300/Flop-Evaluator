def hasDraw(board):
    if max(board) - min(board) <=4: return True
    return False


def straightDraw(board):
    draw = hasDraw(board[0:4])
    if not draw:
        draw = hasDraw(board[1:5])
    if not draw and 14 in board:
        temp = board[:]
        temp.remove(14)
        temp.insert(0,1)
        draw = hasDraw(temp[0:4])
        if not draw:
            draw = hasDraw(temp[1:5])
    return draw

def hasOESD(board):
    i = 1
    while i < 4:
        if board[i] - board[i - 1] != 1: return False
        i += 1
    return True
def OESD(board):
    oesd = hasOESD(board[0:4])
    if not oesd:
        oesd = hasOESD(board[1:5])
    return oesd

def isStraight(board):
    if board[4] == "14" and board[0] == '2' and board[1] == '3' and board[2] == '4' and board[3] == '5': return True
    i = 1
    while i < 5:
        if board[i] - board[i - 1] != 1: return False
        i += 1
    return True

def hasSuit(hand, handClass, flopSuit):
    if handClass == 'p' or handClass == 'o':
        if hand[0].suit == flopSuit or hand[1].suit == flopSuit: return True
        else: return False
    else:
        if hand[0].suit == flopSuit: return True
        else: return False

def isFlush(hand, flopSuit):
    for card in hand:
        if card.suit != flopSuit: return False
    return True