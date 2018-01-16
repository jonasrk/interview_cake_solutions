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

def reverse_word_order(input):

    input = reverse_string_in_place(input)

    l = []
    for char in input:
        l.append(char)

    word_start = 0
    word_end = 0
    
    for i in range(0, len(l)):
        if l[i] == ' ':
            word_end = i
            for i in range(word_start, word_end):
                # swap start
                helper = l[i]
                l[i] = l[len(l) - 1 - i] 
                l[len(l) - 1 - i] = helper
                # swap end
            word_start = i+1

    s = ''
    for el in l:
        s = s + el

    return s

    
            

print(reverse_word_order("los hier ist was Hallo"))
