def reverse_string_in_place(input):
    l = []
    for char in input:
        l.append(char)

    for i in range(0, len(l)//2):
        # swap start
        helper = l[i]
        l[i] = l[len(l) - 1 - i] 
        l[len(l) - 1 - i] = helper
        # swap end

    s = ''
    for el in l:
        s = s + el

    return s

print(reverse_string_in_place("Jonas Kemper"))
