import glob

modules = glob.glob('allRanges/*.py')
from .allRanges import *


def getRange(pos1, pos2, action):
    a, b = None, None
    print(pos1)
    print(pos2)
    print(action)
    if action == 'SRP':
        if pos1 == 'BU': a, b = BUBB2()
        if pos1 == 'CO': a, b = COBB2()
        if pos1 == 'HJ': a, b = HJBB2()
        if pos1 == 'UTG':
            if pos2 == 'BB': a, b = UTGBB2()
            if pos2 == 'BU': a, b = UTGBU2()
        if pos1 == 'SB': a, b = SBBB2()

    if action == '3BP':
        if pos1 == 'SB':
            if pos2 == 'BU': a, b = SBBU3()
            if pos2 == 'CO': a, b = SBCO3()
            if pos2 == 'UTG/HJ': a, b = SBUTG3()
        if pos1 == 'HJ':
            if pos2 == 'UTG':  a, b = HJUTG3()

        if pos1 == 'CO': a, b = COUTG3()

        if pos1 == 'BU':
            if pos2 == 'CO':  a, b = BUCO3()
            if pos2 == 'UTG/HJ':  a, b = BUUTG3()

        if pos1 == 'BB':
            if pos2 == 'SB': a, b = BBSB3()
            if pos2 == 'UTG/HJ': a, b = BBUTG3()
            if pos2 == 'CO': a, b = BBCO3()
            if pos2 == 'BU': a, b = BBBU3()



    if action == '4BP':
        if pos1 == 'UTG':
            if pos2 == 'CO': a, b = UTGCO4()
            if pos2 == 'BU': a, b = UTGBU4()
        if pos1 == 'CO':
            if pos2 == 'BU': a, b = COBU4()
        if pos1 == 'SB':
            if pos2 == 'BB': a, b = SBBB4()
    return a,b


