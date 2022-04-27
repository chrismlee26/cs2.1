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
    items_list += items1[i:] + items2[j:]
    return items_list

merge1 = [0, 1, 2, 3, 4]
merge2 = [5, 6, 7, 8, 9]

# print(merge(merge1, merge2))

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    left, right = [], []
    i, j = 0, 0

    if len(items) <= 1: 
        return items
    else:
        # count index and split /2 
        # i = 1st half index
        # j = 2nd half index

        # if ?
        # use i index to append items to left arr
        # perform iterative sort algorithm on left 
            # return left
        
        # if ?
        # use j index to append items to right arr
        # perform iterative sort algorithm on right
            # return right

        # merge sorted halves
        pass


# ss_merge_test = [2, 9, 6, 3, 0, 5, 4, 1, 7, 8]
# print(split_sort_merge(ss_merge_test))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""


    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) > 1:
        # TODO: Split items list into approximately equal halves
        mid = len(items) // 2 
        left = items[:mid] 
        right = items[mid:]

        i, j = 0

        # TODO: Sort each half by recursively calling merge sort
        merge_sort(left) 
        merge_sort(right)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
        #     output[k] = X[i]
        #     i += 1
        #   else: y[j] < x[i]:
        #     output[k] = y[j]
        #     j += 1
        
        # TODO: Merge sorted halves into one list in sorted order
                pass
            pass
    pass

merge_sort_items = [12, 2, 6, 11, 55, 99, 5, 25, 89]
print(merge_sort(merge_sort_items))



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
    pivot = items[high]
    i = low - 1

    for j in range(low, high):
        if items[j] <= pivot:
            i += 1
            items[i], items[j] = items[high], items[i+1]
    return i + 1

    # for i in range(low, high):
    #     if items[i] <= items[high]:
    #         items[i], items[low] = items[high], items[i]
    #         low += 1
    # items[high], items[low] = items[low], items[high]
    # return low

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions? O(n log n)
    TODO: Worst case running time: ??? Why and under what conditions? O(n^2)
    TODO: Memory usage: ??? Why and under what conditions? O(n)"""

    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)

    # TODO: Partition items in-place around a pivot and get index of pivot
    if low < high:
        pivot_item  = partition(items, low, high)
    # TODO: Sort each sublist range by recursively calling quick sort
        quick_sort(items, low, pivot_item - 1)
        quick_sort(items, low, pivot_item + 1, high)
    return quick_sort(qs_items)

qs_items = [12, 2, 6, 11, 55, 99, 5, 25, 89]
# print(partition(qs_items, 0, len(qs_items)-1))

# print("Unsorted Array:", qs_items) 
# print(quick_sort(qs_items, 0, len(qs_items)-1))
# print("Sorted Array:", qs_items)


