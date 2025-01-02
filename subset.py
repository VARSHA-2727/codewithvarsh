def is_subset(a, b):
    # Convert array a[] into a set for faster lookup
    set_a = set(a)
    
    # Check if any element in b[] is not in set_a
    for element in b:
        if element not in set_a:
            return False  # If any element is not in a[], return False
    return True  # If all elements are found in a[], return True

# Example usage
a = [1, 2, 3, 4, 5]
b = [2, 4]
print(is_subset(a, b))  # Output: True

b = [6, 7]
print(is_subset(a, b))  # Output: False
