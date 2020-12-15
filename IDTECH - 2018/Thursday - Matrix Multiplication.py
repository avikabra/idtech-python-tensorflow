import numpy as np
A = np.array([[0.3, 0.1], [0.2, 0.2]])
print(A)
learningRate = float(input("What is the learning rate"))
A = A - A*learningRate
print(A)