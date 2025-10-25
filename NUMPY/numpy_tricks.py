import numpy as np

# 1. Array Creation Tricks
print("=== Array Creation ===")
# Quick arrays
zeros = np.zeros(5)
ones = np.ones((2,3))
range_arr = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)
print(f"Zeros: {zeros}")
print(f"Range: {range_arr}")

# 2. Indexing Tricks
print("\n=== Indexing Tricks ===")
arr = np.array([1, 2, 3, 4, 5, 6])
# Boolean indexing
mask = arr > 3
print(f"Elements > 3: {arr[mask]}")
# Fancy indexing
indices = [0, 2, 4]
print(f"Selected indices: {arr[indices]}")

# 3. Broadcasting
print("\n=== Broadcasting ===")
a = np.array([[1, 2, 3]])
b = np.array([[1], [2], [3]])
result = a + b
print(f"Broadcasting result:\n{result}")

# 4. Vectorization
print("\n=== Vectorization ===")
# Instead of loops, use vectorized operations
arr = np.array([1, 4, 9, 16])
sqrt_arr = np.sqrt(arr)
print(f"Square roots: {sqrt_arr}")

# 5. Array Manipulation
print("\n=== Array Manipulation ===")
arr = np.array([[1, 2], [3, 4]])
# Reshape
reshaped = arr.reshape(-1)  # -1 means infer dimension
print(f"Flattened: {reshaped}")
# Stack arrays
stacked = np.vstack([arr, arr])
print(f"Stacked:\n{stacked}")

# 6. Statistical Operations
print("\n=== Statistics ===")
data = np.random.randint(1, 10, 10)
print(f"Data: {data}")
print(f"Mean: {np.mean(data):.2f}")
print(f"Std: {np.std(data):.2f}")
print(f"Percentile 75: {np.percentile(data, 75)}")

# 7. Conditional Operations
print("\n=== Conditional Operations ===")
arr = np.array([1, -2, 3, -4, 5])
# Replace negative values with 0
result = np.where(arr < 0, 0, arr)
print(f"Replace negatives: {result}")

# 8. Memory Efficient Operations
print("\n=== Memory Tricks ===")
# Use views instead of copies when possible
original = np.array([1, 2, 3, 4, 5])
view = original[::2]  # Every 2nd element (view)
copy = original[::2].copy()  # Actual copy
print(f"View: {view}")

# 9. Advanced Indexing
print("\n=== Advanced Indexing ===")
arr = np.random.randint(1, 10, (3, 3))
print(f"Array:\n{arr}")
# Get diagonal elements
diagonal = np.diag(arr)
print(f"Diagonal: {diagonal}")

# 10. Performance Tips
print("\n=== Performance Tips ===")
# Use np.dot for matrix multiplication
a = np.random.rand(100, 100)
b = np.random.rand(100, 100)
# Fast matrix multiplication
result = np.dot(a, b)
print(f"Matrix mult shape: {result.shape}")
