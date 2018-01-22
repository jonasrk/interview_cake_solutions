def two_eggs(lo, hi, eggs, tries):

    tries += 1

    storey_range = hi - lo
    halve = storey_range // 2
    
    if breaks_at(lo + halve):
        eggs -= 1
   
    if eggs == 2:
        return two_eggs(lo + halve, hi, 2, tries)
    elif eggs < 2:
        for i in range(lo, lo + halve + 1):
            tries += 1
            if breaks_at(i):
                return i, tries

def breaks_at(height):
    if height >= 76:
        return True
    else:
        return False


print(two_eggs(1, 100, 2, 0))
