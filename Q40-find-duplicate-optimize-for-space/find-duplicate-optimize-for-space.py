def find_repeat(the_list):
    has_repeated = False
    index = the_list[0]
    while not has_repeated:
        old_index = index
        index = the_list[index]
        the_list[old_index] = '_'
        if the_list[index] == '_':
            has_repeated = True

    return index, the_list

print(find_repeat([3, 1, 2, 3, 4, 5, 6, 7, 8, 9]))