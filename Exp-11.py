import pandas as pd
import numpy as np

# 1. Create a Series of 10 random numbers
s = pd.Series(np.random.randint(1, 100, 10))
print("Original Series:")
print(s)

# 2. Indexing
print("\nFirst element:", s[0])
print("First five elements:")
print(s[:5])

# 3. Filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# 4. Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())