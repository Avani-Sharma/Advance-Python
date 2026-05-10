import numpy as np
# Q1. Create a One-Dimensional Array
# Create a NumPy array containing values from 1 to 10. Then:
arr = np.array([1,2,3,4,5,6,7,8,9,10])
# 1. Print the shape
print(arr.shape)
# 2. Print the size
print(arr.size)
# 3. Print the number of dimensions
print(arr.ndim)

print()

# Q2. Create Arrays Using NumPy Function . Create:
# 1. A 3×3 matrix of zeros
print(np.zeros((3,3)))
# 2. A 2×4 matrix of ones
print(np.ones((2,4)))
# 3. A 4×4 identity matrix
print(np.eye((4)))

print()

# Q3. arange() vs linspace()
# 1. Create an array from 0 to 20 with step size 2 using arange()
print(np.arange(0, 21, 2))
# 2. Create 5 equally spaced values between 0 and 20 using linspace()
print(np.linspace(0, 20, 5))

print()

# Q4. Data Types :  Create:
arr1 = np.array([1,2,3,4])
# Then:
# 1. Check datatype
print(arr1.dtype)
# 2. Convert datatype to float
print(arr1.astype(float))

print()

# Q5. Basic Indexing Given:
arr2 = np.array([10,20,30,40,50])
# Perform:
# 1. Print first element
print(arr2[0])
# 2. Print last element
print(arr2[-1])
# 3. Print middle element
arr2[len(arr2)//2]
# 4. Reverse the array
print(arr2[::-1])

print()

# Q6. Basic Slicing
# Using the same array:
# 1. Extract first 3 elements
print(arr2[:3])
# 2. Extract last 2 elements
print(arr2[-2:])
# 3. Extract elements from index 1 to 4
print(arr2[1:5])
# 4. Extract every second element
print(arr2[::2])

print()

# Q7. Matrix Indexing
arr3 = np.array([
        [1,2,3],
        [4,5,6],
        [7,8,9]])
# Perform:
# 1. Print element 5
print(arr3[1,1])
# 2. Print second row
print(arr3[1])
# 3. Print third column
print(arr3[:, 2])
# 4. Print last row using negative indexing
print(arr3[-1])

print()

# Q8. Matrix Slicing
# Using the same matrix:
# 1. Extract:
# [[1,2],
# [4,5]]
print(arr3[:2, :2])
# 2. Extract:
# [[5,6],
# [8,9]]
print(arr3[1:, 1:])
# 3. Extract corner elements [1,3,7,9]
print(arr3[::2, ::2])

print()

# Q9. Reverse Rows & Columns
arr4 = np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
# 1. Reverse rows
print(arr4[::-1])
# 2. Reverse columns
print(arr4[:, ::-1])
# 3. Reverse both rows and columns
print(arr4[::-1, ::-1])

print()

# Q10. Filtering Values
arr5 = np.array([5,10,15,20,25,30])
# 1. Extract values greater than 15
print(arr5[arr5>15])
# 2. Extract even numbers
print(arr5[arr5 %2==0])
# 3. Replace values greater than 20 with 0
arr5[arr5>20 ] = 0
print(arr5)

print()

# Q11. Boolean Indexing in Matrix
arr6 = np.array([
        [10,20,30],
        [40,50,60]])
# 1. Extract values greater than 25
print(arr6[arr6>25])
# 2. Replace values greater than 25 with -1
arr6[arr6>25] = -1
print(arr6)

print()

# Q12. Scalar Broadcasting
# Add 10 to: [1,2,3,4]
arr7 = np.array([1,2,3,4])
print(10+ arr7)

print()

# Q13. Row-wise Broadcasting
A = np.array([
        [10,20,30],
        [40,50,60] 
        ])
B = np.array([1,2,3])
# Add B to A .
print(B+A)

print()

# Q14. Column-wise Broadcasting
A = np.array([
            [10,20,30],
            [40,50,60]])
B = np.array([
            [1],
            [2]])
# Add B to A .
print(B+A)

print()

# Q15. Broadcasting Validity
# Check whether these operations are valid:
# 1. (2,3) + (3,)
print("it's valid")
# 2. (3,2) + (2,)
print("it's valid")
# 3. (2,3) + (2,)
print("it's not valid")

print()

# Q16. Sum Operations
arr8 = np.array([
        [1,2,3],
        [4,5,6]
        ])
# 1. Total sum
print(arr8.sum())
# 2. Row-wise sum
print(arr8.sum(axis = 1))
# 3. Column-wise sum
print(arr8.sum(axis = 0))

print()

# Q17. Statistical Operations
# Using the same matrix:
# 1. Mean of each row
print(arr8.mean(axis = 1))
# 2. Mean of each column
print(arr8.mean(axis = 0))
# 3. Maximum value in each row
print(arr8.max(axis = 1))
# 4. Minimum value in each column
print(arr8.min(axis = 0))

print()

# Q18. Find standard deviation of
arr9 = np.array([10,20,30,40,50])
print(arr9.std())

print()

# Q19. Reshaping
a1 = np.array([1,2,3,4,5,6])
# 1. Convert into 2×3 matrix
print(a1.reshape(2,3))
# 2. Convert into 3×2 matrix
print(a1.reshape(3,2))
# 3. Convert into column vector
print(a1.reshape(6,1))

print()

# Q20. Flattening
a2 = np.array([[1,2,3],
            [4,5,6]])
# 1. Flatten using flatten()
print(a2.flatten())
# 2. Flatten using ravel()
print(a2.ravel())

print()

# Q21. Observe Memory Sharing
a = np.array([1,2,3])
b = a
b[0] = 100
# 1. Print a
print(a)

print()

# Q22. Create Independent Copy
# Modify previous code so changing b does not affect a .
c = np.array([1,2,3])
d = c.copy()
d[0] = 100
# 1. Print a
print(c)
print(d)

print()

# Q23. Min-Max Normalization
ar1 = np.array([10,20,30,40,50])
# between 0 and 1.
print((ar1 - ar1.min()) /(ar1.max()-ar1.min()))

print()

# Q24. Matrix Normalization
ar2 = np.array([[1,2],
            [3,4]])
print((ar2 - ar2.min()) /(ar2.max()-ar2.min()))

print()

# Q25. Column-wise Normalization
ar3 = np.array([[10,100],
            [20,200],
            [30,300]])
print((ar3 - ar3.min(axis = 0)) /(ar3.max(axis=0)-ar3.min(axis=0)))

print()

# Q26. Generate Random Float Values
# 1. A single random float between 0 and 1
print(np.random.rand())
# 2. An array of 5 random float values
print(np.random.rand(5))

print()

# Q27. Random Integer Array
# 1. 5 random integers between 1 and 10
print(np.random.randint(1,11, 5))
# 2. A 3×3 matrix of random integers between 50 and 100
print(np.random.randint(50, 101, (3,3)))

print()

# Q28. Random Choice
array = np.array([10,20,30,40,50])
# Randomly select:
# 1. One value
print(np.random.choice(array))
# 2. Three values
print(np.random.choice(array, 3))

print()

# Q29. Random Normal Distribution
# 1. 5 random values from normal distribution
print(np.random.randn(5))
# 2. A 2×3 matrix using randn()
print(np.random.randn(2,3))

print()

# Q30. Set Random Seed
# Generate random integers between 1 and 100 using:
# np.random.seed()
np.random.seed(42)
print(np.random.randint(1, 101, 5))

print()

# Q31. Permutation
array4 = np.array([1,2,3,4,5])
# 1. Generate a permutation of the array
perm = np.random.permutation(array4)
print("Permutation:", perm)
# 2. Compare permutation with shuffle
np.random.shuffle(array4)
print("Shuffled array:", array4)

print()

# Q32. Random Matrix Statistics
# Generate a 4×4 matrix of random integers between 1 and 50.
mat = np.random.randint(1, 51, (4,4))
# 1. Find maximum value
print(np.max(mat))
# 2. Find minimum value
print(np.min(mat))
# 3. Find row-wise sum
print(np.max(mat, axis =1))
# 4. Find column-wise mean
print(np.max(mat, axis=0))

print()

# Q33. Random Filtering
# Generate 10 random integers between 1 and 100.
mat1 = np.random.randint(1, 101, 10)
# 1. Extract even numbers
print(mat1[mat1 %2==0])
# 2. Extract values greater than 50
print(mat1[mat1 >50])
# 3. Replace values less than 30 with 0
mat1[mat1<30] = 0
print(mat1)

print()

# Q34. Random Normalization Challenge
# Generate a random array of size 8.
# Normalize all values between 0 and 1.
array8 = np.random.rand(8)
print("Original:", array8)
normalized = (array8 - np.min(array8)) / (np.max(array8) - np.min(array8))
print("Normalized:", normalized)

print()

# Q35. Create a 5×5 matrix with values from 1 to 25.
mat5 = np.arange(1, 26).reshape(5,5)
# 1. Print diagonal elements
print(np.diag(mat5))
# 2. Replace diagonal elements with 0
np.fill_diagonal(mat5, 0)
print(mat5)

print()

# Q36.without manually typing rows.
# [[1,1,1],
# [2,2,2],
# [3,3,3]]
D = np.arange(1,4).reshape(3,1)
result = np.repeat(D, 3, axis=1)
print(result)

print()

# Q37. Generate a random matrix and:
mat9 = np.random.randint(1, 101, (3,3))
# 1. Reverse rows
print(mat9[::-1])
# 2. Reverse columns
print(mat9[:, ::-1])
# 3. Flatten the matrix
print(mat9.flatten())

print()

# Q38. Generate a random 3×3 matrix and extract:
matr = np.random.randint(1, 51, (3,3))
# 1. First row
# 2. Last column
# 3. Center element
# 4. Corner elements
print(matr[0])
print(matr[:, -1])
print(matr[1,1])
print(matr[::2, ::2])