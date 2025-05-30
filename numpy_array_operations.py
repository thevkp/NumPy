import numpy as np


a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

# print(a1)
# print(a2)



#Scalar Multiplication
a1 = a1 * 2
print(a1)

# Multiplication of two numpy arrays
a3 = a1 * a2
print(a3)

a31 = np.array([[a1[i][j] * a2[i][j] for j in range(a1.shape[1])] for i in range(a1.shape[0])])
print(a31)
# print(a3 == a31

#Relation operation
print(a1 > 2)
print(a2 == 14)

#Vector operation
a4 = a1 + a2
print(a4)