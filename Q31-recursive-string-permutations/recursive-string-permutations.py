def perms(input):
    if len(input) == 2:
        a = '' + input[0] + input[1]
        b = '' + input[1] + input[0]
        return [a, b]
    else:
        output = []
        for i, char in enumerate(input):
            for perm in perms(input[:i] + input[i+1:]):
                output.append(char + perm)

        return output

print(perms('1234'))

