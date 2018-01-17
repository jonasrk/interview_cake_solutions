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
        if  i == len(l) - 1 or l[i + 1] == ' ':
            word_len = i + 1 - word_start
            for j in range(word_start, word_start + word_len//2):
                # swap start
                word_index = j - word_start
                helper = l[j]
                l[j] = l[word_start + word_len - 1 - word_index] 
                l[word_start + word_len - 1 - word_index] = helper
                # swap end
            word_start = i+2

    s = ''
    for el in l:
        s = s + el

    return s

print(reverse_word_order("los hier ist was Hallo"))

# conplexity: O(n) time / O(1) space
