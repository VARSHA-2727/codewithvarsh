def left_rotate(arr, k):
    n = len(arr)
    k = k % n  # Ensure k is within the bounds
    rotated_arr = []
    rotated_arr.extend(arr[k:])
    rotated_arr.extend(arr[:k])
    return rotated_arr

# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = left_rotate(arr, k)
print(rotated_arr)
    
