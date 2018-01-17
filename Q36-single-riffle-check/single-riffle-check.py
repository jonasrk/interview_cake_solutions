def is_single_riffle(shuffled_deck, half1, half2):
    while len(shuffled_deck) > 0:
        card = shuffled_deck.pop()
        if len(half1) > 0 and half1[-1] == card:
            half1.pop()
        elif len(half2) > 0 and half2[-1] == card:
            half2.pop()
        else:
            return False
    if len(half1) == 0 and len(half2) == 0:
        return True
    else:
        return False

print(is_single_riffle([1,2,3], [3,1,2], [3]))

# complexity: O(n) time / O(1) space
