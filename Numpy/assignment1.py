import numpy as np
# Q1. One-Dimensional Array
# Create an array [10, 20, 30, 40, 50]
# Perform:
# 1. Print first element
# 2. Print last element
# 3. Print elements from index 1 to 3
# 4. Reverse the array
a = [10, 20, 30, 40, 50]
print("first element:", a[0])
print("last element:", a[-1])
print("element from index 1 to 3", a[1:4])
print("reverse:", a[::-1])

print()

# Q2. Matrix Basics
# Create a 2×3 matrix using np.arange(1,7)
# 1. Print shape
# 2. Print second row
# 3. Print first column
b = np.arange(1,7).reshape(2,3)
print("shape:", b.shape)
print("second row:", b[1])
print("first col:", b[:, 0])

print()

# Q3. Basic 1D Slicing
# Given: arr = np.array([1,2,3,4,5,6])
# Perform:
# 1. Extract elements from index 1 to 4
# 2. Extract first 3 elements
# 3. Extract last 3 elements
# 4. Reverse the array using slicing
c = np.array([1,2,3,4,5,6])
print("index 1 to 4:", c[1:5])
print("first 3 elements:", c[:3])
print("last 3 elements:", c[-3:])
print("reverse:", c[::-1])

print()

# Q4. Step Slicing
# Using the same array:
# 1. Extract every 2nd element
# 2. Extract elements in reverse order with step
# 3. Extract elements starting from index 1 with step 2
d = np.array([1,2,3,4,5,6])
print("every 2 element:", d[::2])
print("reverse:", d[::-1])
print("index 1 with step 2:",d[1::2])

print()

# Q5. 2D Slicing (Sub-matrix)
# Extract:
# 1. First two rows and first two columns
# 2. Last two rows and last two columns
# 3. Entire second row
# 4. Entire third column
e = np.array([
            [10,20,30],
            [40,50,60],
            [70,80,90]
        ])
print("First two rows and first two columns:", e[:2, :2])
print("Last two rows and last two columns:", e[1:, 1:])
print("Entire second row:", e[1, :])
print("Entire third column:", e[:, 2])

print()

# Q6. Advanced 2D Slicing
# From the same matrix:
# 1. Extract:
# [[20,30],
# [50,60]]
f = np.array([
            [10,20,30],
            [40,50,60],
            [70,80,90]
        ])
print("extract:", f[:2, 1:])
# 2. Extract:
# [[10,30],
# [70,90]]
print("extract:", f[::2, ::2])
# 3. Reverse: rows , columns
print("reverse row :",f[::-1])
print("reverse col:", f[:, ::-1])
print("reverse both row col:", f[::-1, ::-1])

print()

# Q7. Negative Indexing + Slicing
# arr = np.array([10,20,30,40,50])
# Perform:
# 1. Extract last 2 elements
# 2. Extract all elements except last one
# 3. Reverse using negative slicing
g = np.array([10,20,30,40,50])
print("last 2 elements:", g[-2:])
print("all elements except last one:", g[:-1])
print("reverse:", g[::-1])

print()

# Q8 arr = np.array([10,20,30,40,50])
# 1. Extract values greater than 25
# 2. Replace values greater than 25 with 0
h = np.array([10,20,30,40,50])
print("greater than 25: ", h[h>25])
h[h>25]=0   #replace value with 0
print("greater than 25 and replace values with 0: ", h )

print()

# Q9 Add [1,2,3] to:
i = np.array([[10,20,30],
        [40,50,60]])
print("addition:", i + [1,2,3])

print()

# Q10 Add column vector:
j = np.array([[10,20,30],
        [40,50,60]])
col = np.array([[1],
            [2]])
print("column vector add:", j + col )

print()

# Q11
k = np.array([[1,2,3],
        [4,5,6]])
# 1. Find total sum
# 2. Find column-wise sum
# 3. Find row-wise sum
print("total sum:", k.sum())
print("column sum:", k.sum(axis = 0))
print("row sum:", k.sum(axis=1))

print()

# Q12
# 1. Mean of each row
# 2. Maximum of each column
l = np.array([[1,2,3],
        [4,5,6]])
print("mean of each row:", l.mean(axis = 1) )
print("max of each col:", l.max(axis = 0))

print()

# Q13 Convert:
# [1,2,3,4,5,6]
# into:
# 1. 2×3 matrix
# 2. 3×2 matrix
m = np.array([1,2,3,4,5,6])
print("2×3 matrix:", m.reshape(2,3))
print("3×2 matrix:", m.reshape(3,2))

print()

# Q14
# Flatten:
n = np.array([[1,2,3],
        [4,5,6]])
print("flatten:", n.flatten())

print()

# Q15 Run:
o = np.array([1,2,3])
p = o
p[0] = 100
# 1. What is value of o ?
print("value of o:", o)
# 2. Why?
print("Because p and o refer to the same array in memory.")

# Q16 Fix above using .copy()
q = np.array([1,2,3])
r = q.copy()   
r[0] = 100
print("q:", q)
print("r:", r)

# Q17 Extract:
# 1. Middle row
# 2. Middle column
# 3. Corners → [1,3,7,9]
s = np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
print("middle row:", s[1])
print("middle col:", s[:, 1])
print("corners:", s[::2, ::2] )

print()

# Q18 create: 
# [[1,1,1],
# [2,2,2],
# [3,3,3]] Without manually typing rows
t = np.array([1,2,3]).reshape(3,1)
result = t * np.ones((1,3), dtype=int)
print(result)