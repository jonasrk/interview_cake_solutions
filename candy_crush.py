class Index:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findMatches(entries):

    results = []

    # iterate over rows
    for i in range(0, len(entries[0])):
        occurences = 1
        for j in range(1, len(entries)):
            if entries[j][i] == entries[j - 1][i]:
                occurences += 1
                if j == len(entries[i]) - 1 and occurences >= 3:
                    # reached an end position
                    sequence = [[j - 2, i], [j, i]]
                    results.append(sequence)
            else:
                if occurences >= 3:
                    # reached an end position
                    sequence = [[j - 3, i], [j - 1, i]]
                    results.append(sequence)


    # iterate over cols
    for j in range(0, len(entries[0])):
        occurences = 1
        for i in range(1, len(entries)):
            if entries[j][i] == entries[j][i-1]:
                occurences += 1
                if i == len(entries) - 1 and occurences >= 3:
                    # reached an end position
                    sequence = [[j, i - occurences + 1], [j, i]]
                    results.append(sequence)
            else:
                if occurences >= 3:
                    # reached an end position
                    sequence = [[j, i - occurences], [j, i - 1]]
                    results.append(sequence)

    return results


# 0 1 2 3
# A A A C 0
# B B C D 1
# D B C D 2
# B B B B 3

# [[I(0, 0], I(2, 0)],
# [I(0, 3], I(3, 3)],
# [I(1, 0], I(1, 3)]]

print(findMatches([['A', 'A', 'A', 'C'],
                   ['B', 'B', 'C', 'D'],
                   ['D', 'B', 'C', 'D'],
                   ['B', 'B', 'B', 'B']]))