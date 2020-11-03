def findBreakdown(res, breakdown, pairDict, nonPairDict, weight):
    if 'NUTS' in res:
        breakdown['Nuts'] += weight
    elif 'PAIR' in res:
        breakdown['All Pairs'] += weight
        for idx, val in enumerate(res['PAIR']):
            if val:
                for k in pairDict[idx]:
                    breakdown[k] += weight
    else:
        for idx, val in enumerate(res['NOPAIR']):
            if val:
                for k in nonPairDict[idx]:
                    breakdown[k] += weight
    return breakdown


def finalDict(res, w):
    return {k:(str(( int((v/w) *100* 100) / 100)) + '%') for k, v in res.items()}