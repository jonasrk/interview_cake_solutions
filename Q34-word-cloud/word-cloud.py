def count_words(input, result):
    result = {}d
    for word in input.split(' '):
        l_word = ''.join(e for e in word.lower() if (e.isalnum() or e == '-')) 
        if l_word in result:
            result[l_word] += 1
        else:
            result[l_word] = 1

    return result

s1 = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
s2 = "The bill came to five dollars."

results = count_words(s1, {}) 
results = count_words(s2, results) 

print(results)
