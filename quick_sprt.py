def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    hight = last
    while low < hight:
        while low < hight and alist[hight] >= mid_value:
            hight -= 1
        alist[low] = alist[hight]
        while low < hight and alist[low] <= mid_value:
            low += 1
        alist[hight] = alist[low]
    alist[low] = mid_value
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


alist = [1, 33, 4, 54, 3, 90, 888, 232, 5, 7, 54, 657]


# print(alist)
# quick_sort(alist, 0, len(alist)-1)
# print(alist)

def quick_sort_test0(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    hight = last
    while low < hight:
        while low < hight and alist[hight] >= mid_value:
            hight -= 1
        alist[low] = alist[hight]
        while low < hight and alist[low] <= mid_value:
            low += 1
        alist[hight] = alist[low]
    alist[low] = mid_value
    quick_sort_test0(alist, first, low - 1)
    quick_sort_test0(alist, low + 1, last)


print(alist)
quick_sort_test0(alist, 0, len(alist) - 1)
print(alist)
