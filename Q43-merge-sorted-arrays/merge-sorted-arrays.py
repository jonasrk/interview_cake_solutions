def merge_lists(listA, listB):
	result = []
	while len(listA) + len(listB) > 0:
		if len(listA) == 0:
			result = [listB.pop()] + result 
		elif len(listB) == 0:
			result = [listA.pop()] + result 
		else:
			if listA[-1] > listB[-1]:
				result = [listA.pop()] + result
			else:
				result = [listB.pop()] + result
	return result

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
