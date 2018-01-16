def find_unique(l):
    s = set()
    for el in l:
        if el in s:
            s.remove(el)
        else:
            s.add(el)
    return s

delivery_id_confirmations = [1,2,1,2,3,4,4]

print(find_unique(delivery_id_confirmations))
