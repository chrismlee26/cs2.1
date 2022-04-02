inputs = [3, 12, 25, 34, 99]

def binary_search(inputs, low, high, query):
    if high >= low:
        midpoint = (high + low ) // 2
        if inputs[midpoint] == query:
            return midpoint
        elif inputs[midpoint] > query:
            return binary_search(inputs, low, midpoint-1, query)
        else:
            return binary_search(inputs, midpoint+1, high, query)
    else:
        return -1

