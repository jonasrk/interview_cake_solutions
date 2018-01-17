def find_corresponding_closing_parenthesis(input):

    stack = []

    for char in input:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')':
            c = stack.pop()
            if c !=  '(':
                return False
        elif char == ']':
            c = stack.pop()
            if c != '[':
                return False
        elif char == '}':
            c = stack.pop()
            if c != '{':
                return False

    if len(stack) > 0:
        return False
    else:
        return True

input = '{ [ ] ( ) }'
print(find_corresponding_closing_parenthesis(input))
input = '{ [ ( ] ) }'
print(find_corresponding_closing_parenthesis(input))
input = '{ [ }'
print(find_corresponding_closing_parenthesis(input))

# complexity: O(n) time / O(n) space