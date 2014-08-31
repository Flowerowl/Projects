"""
time:
    worst:O(nlogn)
    best:O(n)
    avg:O(nlogn)
space:
    O(n)
"""
#encoding:utf-8
origin_list = [6,4,8,2,1,0,8,8,4,1,2,0,8,9,11,2,1]


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        print 'current >>>%s' % merged
        return merged

    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    print 'left >>>%s right >>>%s' % (left, right)
    return merge(left, right)


if __name__ == '__main__':
    print 'origin >>>%s' % origin_list
    merge_sort(origin_list)
