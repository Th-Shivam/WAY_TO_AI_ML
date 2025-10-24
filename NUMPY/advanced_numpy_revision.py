"""
Advanced NumPy Revision - Essential Concepts & Code Examples
"""

import numpy as np

# ============= ARRAY CREATION & MANIPULATION =============

# Advanced array creation
arr = np.arange(24).reshape(2, 3, 4)
print("3D Array:\n", arr)

# Broadcasting
a = np.array([[1, 2, 3]])
b = np.array([[4], [5]])
result = a + b  # (2,3) result
print("Broadcasting result:\n", result)

# ============= INDEXING & SLICING =============

# Boolean indexing
data = np.random.randn(7, 4)
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print("Boolean indexing:", data[names == 'Bob'])

# Fancy indexing
arr = np.arange(32).reshape(8, 4)
print("Fancy indexing:", arr[[1, 5, 7, 2], [0, 3, 1, 2]])

# ============= UNIVERSAL FUNCTIONS =============

# Element-wise operations
x = np.array([1, 2, 3, 4])
print("Square root:", np.sqrt(x))
print("Exponential:", np.exp(x))

# Conditional logic
result = np.where(x > 2, x, -x)
print("Conditional:", result)

# ============= ARRAY OPERATIONS =============

# Aggregations
arr = np.random.randn(5, 4)
print("Mean by axis:", arr.mean(axis=1))
print("Cumulative sum:", arr.cumsum(axis=0))

# Linear algebra
A = np.random.randn(3, 3)
B = np.random.randn(3, 3)
print("Matrix multiplication:", np.dot(A, B))
print("Eigenvalues:", np.linalg.eigvals(A))

# ============= ADVANCED TECHNIQUES =============

# Vectorization example
def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2, axis=1))

points1 = np.random.rand(1000, 2)
points2 = np.random.rand(1000, 2)
distances = distance(points1, points2)

# Memory views and copies
arr = np.arange(10)
view = arr[::2]  # View
copy = arr[::2].copy()  # Copy

# ============= STRUCTURED ARRAYS =============

# Creating structured array
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
people = np.array([('Alice', 25, 55.0), ('Bob', 30, 70.5)], dtype=dt)
print("Structured array:", people['name'])

# ============= PERFORMANCE TIPS =============

# Use views instead of copies when possible
large_arr = np.random.rand(1000, 1000)
subset = large_arr[:500, :500]  # View, not copy

# Vectorized operations are faster
x = np.random.rand(1000000)
# Fast: np.sin(x)
# Slow: [math.sin(xi) for xi in x]

# ============= COMMON PATTERNS =============

# Meshgrid for coordinate arrays
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 3)
X, Y = np.meshgrid(x, y)

# Histogram
data = np.random.randn(1000)
hist, bins = np.histogram(data, bins=50)

# Sorting
arr = np.random.randn(10)
sorted_indices = np.argsort(arr)
print("Sorted indices:", sorted_indices)

print("\n=== Advanced NumPy Revision Complete ===")
