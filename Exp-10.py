#numpy
import numpy as np

# 1. Create an array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Slicing operations
print("First five elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Alternate elements:", arr[::2])
print("Reversed Array:", arr[::-1])

# 3. Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting
print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)