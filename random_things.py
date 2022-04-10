def integer_multiplication(x, y):
  return x * y

x = 5678
y = 1234
# print(integer_multiplication(x, y))

# Merges 2 arrays, assuming both sorted and in order. 
def merge(items1, items2):
    result = [] # Initialize array for results 
    i, j = 0, 0 # Create indexes to loop items starting at 0

    while i < len(items1) and j < len(items2): # outer loop & base condition
        if items1[i] < items2[j]: # If true (& measuring # of items in each array)
            result.append(items1[i]) # Add array item at index i to end of results array
            i += 1 # Count up index by 1 (Addition Assignment)
        # Hardcode second half (assuming array2 is correctly after array1)
        else: # When items 2 < items 1 
            result.append(items2[j]) #Add item at index j to second array
            j += 1 # iterate index to complete all J's
    result += items1[i:] + items2[j:] # result is assigned to both items at indexes
    return result

merge1 = [0, 1, 2, 3, 4]
merge2 = [5, 6, 7, 8, 9]
print(merge(merge1, merge2))