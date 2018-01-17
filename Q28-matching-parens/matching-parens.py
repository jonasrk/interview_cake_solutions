def find_corresponding_closing_parenthesis(input, index):

    count = 0

    for i, char in enumerate(input[index + 1:]):
        if char == ')' and count == 0:
            return index + i + 1
        elif char == ')':
            count -= 1
        elif char == '(':
            count += 1

    return -1

input = 'Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.'

print(find_corresponding_closing_parenthesis(input, 10))

