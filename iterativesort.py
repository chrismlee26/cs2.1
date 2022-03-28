def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    nums = 0
    i = 1
    while i < len(items):
        if(items[i] < items[i-1]):
            nums = 1
        i += 1
    if (not nums):
        return True
    else:
        return False


unsorted_items = [35, 11, 7, 0]
sorted_items = [1, 2, 4, 6]
print("---#1 Check Sorted---")
is_sorted(unsorted_items)
print("Unsorted Items:", unsorted_items, is_sorted(unsorted_items))
is_sorted(sorted_items)
print("Sorted Items:", sorted_items, is_sorted(sorted_items))
print("------")


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions? N^2
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for _ in range(len(items)):  # outer loop
        for j in range(len(items) - 1):  # inner loop, compare integers
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


items = [3, 1, 7, 0]
print("---#2 Bubble Sort---")
print("Initial values:", items)
bubble_sort(items)
print("Sorted values:", items)
print("------")


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions? --- O(n^2)
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    for i in range(len(items)):
        lowest_num = i
        for j in range(i+1, len(items)):
            if items[lowest_num] > items[j]:
                lowest_num = j
        items[i], items[lowest_num] = items[lowest_num], items[i]


ss_items = [99, 12, 4, 55, 9]
print("---#3 Seletion Sort---")
print("Initial values:", ss_items)
selection_sort(ss_items)
print("Sorted values:", ss_items)
print("------")


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(1, len(items)):
        key = items[i]
        j = i-1
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key


is_items = [4, 1, 52, 13, 7]
print("---#4 Insertion Sort---")
print("Initial values:", is_items)
insertion_sort(is_items)
print("Sorted values:", is_items)
print("------")
