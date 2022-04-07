def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    
    items_list = []
    i = 0
    j = 0

    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            items_list.append(items1[i])
            i += 1
        else:
            items_list.append(items2[j])
            j += 1
    items_list = items_list + items1[i:] + items2[j:]
    return items_list

merge1 = [0, 1, 2, 3, 4]
merge2 = [5, 6, 7, 8, 9]

print(merge(merge1, merge2))


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


ss_merge1 = [5, 4, 1, 7, 8]
ss_merge2 = [2, 9, 6, 3, 0]


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    # output = output array (n)
    # k = len(items) <-- index
    # left = items/2 [arr]
    # right = items/2 [arr]
    # i = 1 <-- (x index operator)
    # j = 1 <-- (y index operator)

    # for k == len(items):
    #   if x[i] < y[j]:
    #     output[k] = X[i]
    #     i += 1
    #   else: y[j] < x[i]:
    #     output[k] = y[j]
    #     j += 1


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions? O(n log n)
    TODO: Worst case running time: ??? Why and under what conditions? O(n^2)
    TODO: Memory usage: ??? Why and under what conditions? O(n)"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if len(items) <= 1:
        return items
    else:
        pivot = items[int(len(items) // 2)]
        # print(pivot)
        # if (pivot > items):
        # while pivot > low and


qs_items = [12, 2, 6, 11, 55, 99, 5, 25, 89]
# print(quick_sort(qs_items), "~~~")
