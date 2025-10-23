import numpy as np

# Array Creation
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2], [3, 4]])
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
eye = np.eye(3)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

# Array Properties
print(f"Shape: {arr2.shape}")
print(f"Size: {arr2.size}")
print(f"Dtype: {arr2.dtype}")
print(f"Dimensions: {arr2.ndim}")

# Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
add = a + b
multiply = a * b
dot_product = np.dot(a, b)

# Indexing and Slicing
arr = np.array([0, 1, 2, 3, 4, 5])
element = arr[2]
slice_arr = arr[1:4]
condition = arr[arr > 2]

# Reshaping
original = np.array([1, 2, 3, 4, 5, 6])
reshaped = original.reshape(2, 3)
flattened = reshaped.flatten()

# Statistical Functions
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
std = np.std(data)
max_val = np.max(data)
min_val = np.min(data)
sum_val = np.sum(data)

# Matrix Operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_mult = np.matmul(matrix1, matrix2)
transpose = matrix1.T
inverse = np.linalg.inv(matrix1)

# Random Numbers
random_arr = np.random.random((2, 3))
random_int = np.random.randint(0, 10, size=(2, 3))
normal = np.random.normal(0, 1, (2, 3))

# Broadcasting
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
broadcast_result = a + b

print("NumPy basics file created successfully!")
