def merge_ranges(ranges):
    sth_merged = True
    # while ranges have been merged
    while sth_merged:
        sth_merged = False
        # go through all ranges
        merged = [ranges[0]]
        for range in ranges[1:] :
            # and try to merge them with the ones before them
            range_has_not_merged = True
            for i, merged_range in enumerate(merged):
                if (range[0] >= merged_range[0] and range[0] <= merged_range[1]) or (range[1] >= merged_range[0] and range[1] <= merged_range[1]):
                    # merge ranges
                    merged[i] = merge(merged_range, range)
                    sth_merged = True
                    range_has_not_merged = False
            if range_has_not_merged:
                merged.append(range)
        ranges = merged
    return ranges

def merge(rangeA, rangeB):
    return (min(rangeA[0], rangeB[0]), max(rangeA[1], rangeB[1]))

print(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]))
