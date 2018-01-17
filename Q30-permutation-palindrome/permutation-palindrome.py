def is_palin(input):
    for i in range(0, len(input) // 2):
        if input[i] != input[len(input) - 1 - i]:
            return False
    return True

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

def permutation_palindrome(input):
    for perm in perms(input):
        if is_palin(perm):
            return True
    return False

print(permutation_palindrome('civic'))
print(permutation_palindrome('ivicc'))
print(permutation_palindrome('civil'))
print(permutation_palindrome('livci'))
