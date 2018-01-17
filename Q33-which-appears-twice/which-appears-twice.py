def appears_twice(input):
    n = len(input) - 1
    sum = None
    if n % 2 == 0:
        sum = (n / 2) * (input[0] + input[-1])
    else:
        sum = ((n - 1) / 2) * (input[0] + input[-1]) + input[(len(input)) - 1 / 2]

    in_sum = 0

    for el in input:
        in_sum += el

    return in_sum - sum

input = [1, 2, 3, 2, 4]

# should return 2
print(appears_twice(input))

# complexity: O(n) time / O(1) space
