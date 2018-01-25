def sums(n, list, target):
    if n == 2:
        s = set(list)
        results = []
        for el in list:
            if target - el in s:
                results.append([el, target - el])

        return results
    else:
        results = []
        for el in list:
            for sol in sums(n - 1, list, target - el):
                results.append([el] + sol)

        return results

def sums_non_recursive(n, list, target):
    n_stack = []
    list_stack = []
    target_stack = []
    results = []
    while True:

        if n == 2:
            this_list = list_stack.pop()
            this_target = target_stack.pop()
            s = set(this_list )
            for el in this_list :
                if this_target - el in s:
                    results.append([el, this_target - el])

            return results
        else:
            for el in list:
                target_stack.append(target)
                target = target - el
                n = n - 1

            return results

print(sums(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))