def step(x):
    return 1 if x>0 else 0

def perceptron(x1, x2, w1, w2, b):
    return step(w1*x1 + w2*x2 + b)  

print(perceptron(0, 0, 1, 1, -1))  # Output: 0
print(perceptron(0, 1, 1, 1, -1))  # Output: 0
print(perceptron(1, 0, 1, 1, -1))  # Output: 0
print(perceptron(1, 1, 1, 1, -1))  # Output: 1  