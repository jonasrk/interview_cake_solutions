def permutation_palindrome(input):
    occs = {}
    for char in input:
        if char in occs:
            occs[char] += 1
        else:
            occs[char] = 1

    count_uneven = 0
    for occ in occs:
        if occs[occ] % 2 != 0:
            count_uneven += 1
            if count_uneven > 1:
                return False

    return True


print(permutation_palindrome('civic'))
print(permutation_palindrome('ivicc'))
print(permutation_palindrome('civil'))
print(permutation_palindrome('livci'))

# complexity: O(n) time / O(n) space