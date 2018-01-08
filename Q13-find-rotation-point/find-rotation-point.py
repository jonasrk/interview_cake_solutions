def find_rot_word(list):
    index = len(list) // 2
    step = len(list) // 2
    found = False
    while not found:
        if is_rot_point(list, index):
            return index
        elif list[index] < list[0]:
            index = (index - step) % len(list)
            step = step // 2

        elif list[index] > list[0]:
            index = (index + step) % len(list)
            step = step // 2

def is_rot_point(list, index):
    if list[(index-1)%len(list)] > list[index]:
        return True
    else:
        return False


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print(find_rot_word(words))