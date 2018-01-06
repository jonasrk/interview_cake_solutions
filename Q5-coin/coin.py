def coin(amount=4, denominations=[1,2,3]):
    results = []
    if amount < min(denominations):
        return [{-1: -1}]
    elif amount == min(denominations):
        return [{min(denominations): 1}]
    elif amount > min(denominations):
        for denomination in denominations:
            base_result = {}
            if denomination == amount:
                base_result[denomination] = 1
                results.append(base_result)
            elif denomination < amount:
                base_result[denomination] = 1
                rest = coin(amount - denomination, denominations)
                for sol in rest:
                    sol_result = base_result.copy()
                    if -1 not in sol:
                        for denom in sol:
                            if denom in sol_result:
                                sol_result[denom] += sol[denom]
                            else:
                                sol_result[denom] = sol[denom]
                        if sol_result != {}: # TODO JRK Why was that?
                            results.append(sol_result)
    # return unique dicts TODO

    return results

print(coin())
