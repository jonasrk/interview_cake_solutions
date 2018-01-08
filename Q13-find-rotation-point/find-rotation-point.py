def sort_list(list):
    rot_word = sorted(list)[0]
    return find_rot_word(list, rot_word)

def find_rot_word(list, word):
    index = len(list) // 2
    step = len(list) // 2
    found = False
    while not found:
        if list[index]:
            return index
        elif list[index] < word:
            index = (index - step) % len(list)
            step = step // 2

        elif list[index] > word:
            index = (index + step) % len(list)
            step = step // 2


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

print(sort_list(words))