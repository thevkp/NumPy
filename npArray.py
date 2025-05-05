import numpy as np


arr = np.array([1,2,3,4])
print(arr)
print(type(arr))
print(len(arr))


arrf = np.array(arr, dtype=float)
print(arrf)


arrb = np.array(arr, dtype=bool)
print(arrb)

arrR = np.arange(1, 11)
print(arrR)

arrRev = np.arange(11, 1, -1)
print(arrRev)

#multidimesional array with np.arange()
arrMul = np.arange(16).reshape(2,2,2,2) #will create an array of 2-D arrays
print(arrMul)

print(arrMul.ndim)

arrShape = np.arange(1, 16).reshape(5, 3) # product of arguments of reshape must be equal to size of array obtained
print(arrShape)

arrOnes = np.ones((3,5)) #creates an ndarray of 3x2 with all elements initialized to 1
print(arrOnes)

arrZeroes = np.zeros((3,4)) #same as ones but with zeroes
print(arrZeroes)



arrRand = np.random.random((3,4))
print(arrRand)


#linearly spaced array -> np.linspace(range, count)
arrLinspace = np.linspace(-10, 10, 15) # first two arguments are range, third argument is number of items
print(arrLinspace)

#identity matrix
arrI = np.identity(3, dtype=int)
print(arrI)


# numPy ndarray methods/function


#ndim -> dimesion of ndarray
print(arr.ndim)
print(arrMul.ndim)

#shap -> elements in each dimension
print(arrMul.shape)
print(arr.shape)

arr2d = np.arange(15).reshape(5, 3)
print(arr2d)
print(arr2d.shape)

print(arr2d.size)

print(arr2d.itemsize) # returns memory occupied by each item
print(arr2d.dtype)

arr2d32bits = arr2d.astype(np.int32)
print(arr2d.itemsize)
print(arr2d32bits.itemsize)