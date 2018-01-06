def coin(amount=4, denominations=[1,2,3]):
    results = []
    if amount < min(denominations):
        return [{-1: -1}]
    elif amount == min(denominations):
        return [{min(denominations): 1}]
    elif amount > min(denominations):
        for denomination in denominations:
            one_result = {}
            if denomination == amount:
                one_result[denomination] = 1
            if denomination < amount:
                one_result[denomination] = 1
                rest = coin(amount - denomination, denominations)
                for sol in rest:
                    if -1 not in sol:
                        for denom in sol:
                            if denom in one_result:
                                one_result[int(denom)] += sol[denom]
                            else:
                                one_result = {**one_result, **sol}
                        if one_result != {}:
                            results.append(one_result)
    # return unique dicts

    return [dict(y) for y in set(tuple(sorted(x.items(), key=lambda tup: tup[0]) ) for x in results)]

print(coin())
