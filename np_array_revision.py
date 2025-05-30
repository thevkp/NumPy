import numpy as np


arr =np.array([1,2,0,4])
print(arr)
print(type(arr))
print(len(arr))

arr_bool = np.array(arr, dtype=bool)
print(arr_bool)


#arange: used to create numpy arrays, same as range(loosely)
#syntax: np.arange(start, end, step(optional))
arr_range = np.arange(1, 11, 2)
print(arr_range)


#multimdimensional array with arange
#syntax: np.arange(N).reshape(shape), shape= dimension i.e.. rowsxcols
# np.arange(N) → creates a NumPy array from 0 to N-1
# .reshape(shape) → changes its shape to the dimensions specified
#Note: N = len(shape) i.e N = rows*cols = size of array
arr_mult_dim = np.arange(14).reshape(2,7)
print(arr_mult_dim)


arr_mult_dim1 = np.arange(18).reshape(2,3,3)
print(arr_mult_dim1)

#auto axis: reshape(rows, -1), python automatically find newaxis
arr_mult_dim_auto = np.arange(18).reshape(3, -1)
print(arr_mult_dim_auto)

#array.ndim  ➝  returns an **integer**, not a tuple.
#return value is number of dimension(axes)
print(f'({arr_mult_dim_auto.ndim}, {arr_mult_dim1.ndim}, {arr_mult_dim.ndim})')

#shape: size along each dimension
print(f'{arr_mult_dim.shape}, {arr_mult_dim1.shape}, {arr_mult_dim_auto.shape}')



# array of zeroes of and ones
arr_ones = np.ones((3,4)) #creates an ndarray of 3x2 with all elements initialized to 1
print(arr_ones)

arr_zeroes = np.zeros((3,4))
print(arr_zeroes)

#Random values
arr_rand = np.random.random((3,2))
print(arr_rand)
# print(np.random.random())
# print(np.random.random(3))
# print(np.random.random(3,4)) # tupe argument
arr_rand1 = np.random.rand() #generate a single random value
print(arr_rand1)

arr_rand2 = np.random.rand(3) #generates a numpy.ndarray of 3 random values
print(type(arr_rand2))

arr_rand3 = np.random.rand(3,3) # 3x3 matrix of random values
print(arr_rand3)


#linear space arrays:Instead of jumping around with random values, this creates evenly spaced numbers across an interval.
#syntax: np.linspace(start, stop, N), start, stop are inclusive, N = number of items
arr_linspace = np.linspace(-10, 10, 3)
print(arr_linspace)

arr_linspace1 = np.linspace(-10, 10, 20)
print(arr_linspace1)

arr_linspace_end_excluded = np.linspace(0, 1, 5, endpoint=False)
print(arr_linspace_end_excluded)
# print((arr_linspace_end_excluded).size)

print(arr_linspace.dtype)
arr_linspace1 = arr_linspace1.astype(np.uint32)
print(arr_linspace1)