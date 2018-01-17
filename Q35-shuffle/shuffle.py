import random

def get_random(floor, ceiling):
     return random.randint(floor, ceiling)

def shuffle(input):
    if len(input) == 2:
        r = get_random(0,1)
        if r == 0:
            return [input[1], input[0]]
        else:
            return input
    elif len(input) > 2:
        el = input[0]
        l = shuffle(input[1:])
        i = get_random(0, len(input) - 1)
        return l[:i] + [el] + l[i:]

print(shuffle(['A', 'B', 'C', 'D']))

# complexity: O(n) time / O(n) space
