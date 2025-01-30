
def firstOne(get):
    low, high = 0, 1
    
    # Step 1: Find an upper bound where get(high) == 1
    while get(high) == 0:
        low = high
        high *= 2  # Exponentially increase range

    # Step 2: Perform binary search in the range [low, high]
    while low < high:
        mid = (low + high) // 2
        if get(mid) == 1:
            high = mid  # Move left
        else:
            low = mid + 1  # Move right

    return low
