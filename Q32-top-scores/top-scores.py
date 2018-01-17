unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

def sort_scores(scores, high):
    a = (high + 1) * [0]
    for score in scores:
        a[score] += 1
    
    sorted = []

    for i in range(high, -1, -1):
        for j in range(0, a[i]):
            sorted.append(i)

    return sorted

print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
# returns [91, 89, 65, 53, 41, 37]

# complexity: O(n) time / O(n) space
