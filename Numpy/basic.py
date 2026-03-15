# numpy: it is a python library that is used to manipulate, process and analyze the data.
# NumPy stands for numeric python or numerical python.
import numpy as np

# 1D ARRAY
# Definition: A 1D array is called a vector. It contains elements arranged in a single row.
a = np.array([1, 2, 3])
print("1D Array:", a)
print("Type:", type(a))

print()

# 2D ARRAY
# Definition: A 2D array is called a matrix. It contains rows and columns.
b = np.array([[1,2,3],
              [4,5,6]])
print("2D Array:\n", b)

print()

# 3D ARRAY
# Definition: A 3D array is called a tensor. It contains multiple 2D matrices stacked together.
c = np.array([
    [[1,2,3],
     [4,5,6]],

    [[7,8,9],
     [10,11,12]]
])

print("3D Array:\n", c)

print()

# dtype
# Definition: The dtype parameter is used to specify or convert the data type of array elements.
d = np.array([1,2,3], dtype=bool)
print("Dtype (bool):", d)

print()

# arange
# Definition: np.arange(start, stop, step) generates evenly spaced values within a given range.
e = np.arange(1, 11, 2)
print("Arange:", e)

print()

# reshape
# Definition: reshape() changes the shape of an array without changing its data.
f = np.arange(1, 11).reshape(5,2)
print("Reshape:\n", f)

print()

# ones
# Definition: np.ones() creates an array where all elements are initialized to 1.
g = np.ones((3,4))
print("Ones:\n", g)

print()

# zeros
# Definition: np.zeros() creates an array where all elements are initialized to 0.
h = np.zeros((4,5))
print("Zeros:\n", h)

print()

# random
# Definition: random() generates random numbers between 0 and 1.
i = np.random.random((3,4))
print("Random:\n", i)

print()

# linspace
# Definition: linspace(start, stop, num) generates evenly spaced numbers between start and stop.
j = np.linspace(-10, 10, 10)
print("Linspace:", j)

print()

# identity
# Definition: identity() creates an identity matrix where diagonal elements are 1 and the rest are 0.
k = np.identity(3)
print("Identity Matrix:\n", k)

print()

# empty
# Definition: empty() creates an array without initializing entries, so it may contain random values.
l = np.empty((3,3))
print("Empty Array:\n", l)

print()

# full
# Definition: full() creates an array filled with a specified constant value.
m = np.full((3,3), 7)
print("Full Array:\n", m)



# Array Attributes
a1 = np.arange(10)                     # 1D array
a2 = np.arange(12, dtype=float).reshape(3,4)   # 2D array
a3 = np.arange(8).reshape(2,2,2)       # 3D array

print("Array 1:\n", a1)
print()

print("Array 2:\n", a2)
print()

print("Array 3:\n", a3)
print()

# ndim
# Definition: Returns the number of dimensions of the array
print("Dimension:", a3.ndim)

# shape
# Definition: Returns the shape of the array (size in each dimension)
print("Shape:", a3.shape)

# size
# Definition: Returns the total number of elements in the array
print("Size:", a3.size)

# itemsize
# Definition: Returns the size (in bytes) of each element
print("Itemsize:", a3.itemsize)

# dtype
# Definition: Returns the data type of the array elements
print("Dtype:", a3.dtype)

print()

print("Original dtype:", a3.dtype)
# change datatype
b = a3.astype(np.int32)
print("Converted Array:\n", b)
print("New dtype:", b.dtype)

print()


# Array Operations
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
print("Array 1:\n", a1)
print()
print("Array 2:\n", a2)
print()

# Scalar Operations: means performing an operation between each element of the array 
# and a single constant value (scalar).
print("Scalar Multiplication:\n", a1 * 2)
print()

print("Scalar Addition:\n", a1 + 2)
print()

# Vector Operations (Element-wise Operations): means performing operations between
# two arrays of the same shape. The operation is applied element by element.
print("Vector Addition:\n", a1 + a2)
print()

print("Vector Multiplication:\n", a1 * a2)
print()



# array function
a1 = np.random.random((3,3))
a1 = np.round(a1 * 100)
print(a1)

print()

# max/min/sum/prod
print("Max:", np.max(a1))
print("Min:", np.min(a1))
print("Sum:", np.sum(a1))
print("Product:", np.prod(a1))

print()

# if we want max number in every row -> axis = 1
# axis = 0 -> column operation
print("Max (row wise):", np.max(a1, axis=1))
print("Min (row wise):", np.min(a1, axis=1))
print("Sum (row wise):", np.sum(a1, axis=1))

print()

# mean/median/standard deviation/variance
print("Mean:", np.mean(a1))
print("Median:", np.median(a1))
print("Standard Deviation:", np.std(a1))
print("Variance:", np.var(a1))

print()

# trigonometric functions
print("sin:", np.sin(a1))
print("cos:", np.cos(a1))
print("tan:", np.tan(a1))

print()

# dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
print(np.dot(a2, a3))

print()

# log and exponents
print("Log:", np.log(a1))
print("Exponential:", np.exp(a1))

print()

# round: nearest integer/floor: lower integer/ceil: higher integer
print("Round:", np.round(np.random.random((2,3)) * 100))
print("Floor:", np.floor(np.random.random((2,3)) * 100))
print("Ceil:", np.ceil(np.random.random((2,3)) * 100))




# INDEXING AND SLICING

# 1D ARRAY
a1 = np.arange(10)      
print(a1)

print(a1[0])            # indexing → access first element
print(a1[-1])           # negative indexing → access last element
print(a1[0:5])          # slicing → elements from index 0 to 4

print()


# 2D ARRAY
a2 = np.arange(12).reshape(3,4)   
print(a2)

print(a2[1,0])        # element at row 1 column 0
print(a2[1,3])        # element at row 1 column 3

print(a2[0:2,1:3])    # slicing rows 0-1 and columns 1-2
print(a2[::2, ::3])   # step slicing → skip elements with step size

print()


# 3D ARRAY
a3 = np.arange(8).reshape(2,2,2)   
print(a3)

print(a3[1,0,0])      # element from block1 row0 column0
print(a3[0,0,0])      # element from block0 row0 column0
print(a3[1,0,1])      # element from block1 row0 column1

print(a3[0, ::2])     # slicing inside first block

print()



# iterating

# 1D array iteration
a1 = np.arange(5)
print(a1)

for i in a1:                # iteration → accessing each element one by one
    print(i)

print()


# 2D array iteration
a2 = np.arange(6).reshape(2,3)
print(a2)

for i in a2:                # iterates row by row
    print(i)

print()


# element-wise iteration
for i in np.nditer(a2):     # nditer → iterate every element of array
    print(i)

print()


# 3D array iteration
a3 = np.arange(8).reshape(2,2,2)
print(a3)

for i in np.nditer(a3):     # iterates each element in 3D array
    print(i)



# RESHAPE / TRANSPOSE / RAVEL
a1 = np.arange(12)
print(a1)

# reshape1: changes shape of array (rows and columns)
a2 = a1.reshape(3,4)     
print(a2)

print()

# transpose: converts rows into columns and columns into rows
print(np.transpose(a2))
print(a2.T)               

print()

# ravel: converts multi-dimensional array into 1D array
print(np.ravel(a2))      



# STACKING ARRAYS
a1 = np.arange(6).reshape(2,3)
a2 = np.arange(6,12).reshape(2,3)
print("Array 1:")
print(a1)
print("Array 2:")
print(a2)

print()

# horizontal stacking
# hstack → joins arrays column wise (side by side)
print(np.hstack((a1, a2)))  

print()

# vertical stacking
# vstack → joins arrays row wise (one above another)
print(np.vstack((a1, a2)))  