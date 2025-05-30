import numpy as np


a1 = np.arange(11)
print(a1)

#indexing

print(a1[-1])


a2 = np.arange(12).reshape(3, 4)
print(a2)


print(a2[1,2])

print(a2[2, 3])
print(a2[1,0])

a3 = np.arange(8).reshape(2,2,2)
print(a3)

print(a3[1, 0, 1])
print(a3[1][0][1])
print(a3[0, 0, 0])
print(a3[1, 1, 0])


#Slicing: fetch multiple items

# 1-D numpy ndarray
a1_slice = a1[2 : 5]
print(a1_slice)
a1_slice = a1[2 : 5 : 2]
print(a1_slice)

a2_slice = a2[0, :] #0-> first row, : -> all columns
print(a2_slice)