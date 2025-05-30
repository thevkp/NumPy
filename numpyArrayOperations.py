import numpy as np


a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

# print(a1)
# print(a2)

# Scalar multiplication
a1 = a1 * 2
print(a1)


# for i in range(a1.shape[0]):
#   for j in range(a2.shape[1]):
#     a2[i][j] = a2[i][j] * a1[i][j]



a2 = np.array([[a1[i][j] * a2[i][j] for j in range(a1.shape[1])] for i in range(a1.shape[0])])

print(a2)


# relation operators
print(a1 > 25)
print(a2 == 26)


#vector operation
a3 = a1 + a2
print(a3)

a4 = a3 * a1
print(a4)

# max/min/prod/sum

print(np.max(a2))
print(np.max(a2[0]))
print(np.max(a1, axis=0)) # print max of each column, 0->column
print(np.max(a1, axis=1)) # print max of each row, 1->row

print(np.min(a2))
print(np.sum(a2))
print(np.prod(a2))


# trig functions
print(np.sin(a1))


# dot product
arr1 = np.arange(12).reshape(3, 4)
arr2 = np.arange(12).reshape(4, 3)
print(np.dot(arr1, arr2))