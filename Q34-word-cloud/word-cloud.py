def count_words(input):
    result = {}
    for word in input.split(' '):
        l_word = ''.join(e for e in word.lower() if (e.isalnum() or e == '-')) 
        if l_word in result:
            result[l_word] += 1
        else:
            result[l_word] = 1

    return result

s = '''After beating the eggs, Dana read the next step: 
Add milk and eggs, then add flour and sugar-bags.'''

print(count_words(s))
