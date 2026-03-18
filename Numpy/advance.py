# # numpy array v/s python list 
# # numpy array is faster than the python list because less memory use, no explicit loop required, 
# # vectorization support, C langauge backend 

# # speed
# print("==================== speed of list=================")
# a = [i for i in range(1000)]
# b = [i for i in range(1000, 2000)]
# c = []
# import time
# start = time.time()
# for i in range(len(a)):
#     c.append(a[i] +b[i])
#     print(time.time()- start)

# print("==================== speed of numpy array =====================")
import numpy as np
# a = np.arange(100000)
# b = np.arange(100000, 200000)
# start = time.time()
# c = a+b
# print(time.time()- start)

# # memory 
# print("==================== memory of list =====================")
# a = [i for i in range(10000000)]
# import sys
# print(sys.getsizeof(a))

# print("=================== memory of numpy array================")
# a = np.arange(1000000, dtype = np.int8)
# print(sys.getsizeof(a))



# # advance indexing
# a= np.arange(24).reshape(6,4)
# print(a)

# # Fancing Indexing: When we select elements from a NumPy array using a list, 
# # tuple, or another array of index positions, it is called Fancy Indexing.
# print("================= Fancy Indexing ================")
# print(a)
# print(a[[0,2,3]])
# print("rows: ", a[[0,2,3,5]])
# print("col: ", a[:, [0, 2, 3]])

# # boolean indexing: When we use a Boolean array (True or False values) to filter or 
# # select elements from a NumPy array, it is called Boolean Indexing.
# # when we works with boolean values use bitwise operators.
# print("=============== Boolean Indexing ================")
# b = np.random.randint(1, 100, 24).reshape(6,4)
# print(b)

# # find all numbers greater than 50
# print("True/False both: ", b>50)
# print("True numbers only:", b[b>50])

# # find all even numbers
# print("True/False both: ", b%2==0)
# print("True numbers only: ", b[b%2==0])

# # find all numbers greater than 50 and even
# print("True/False both: ",(b>50) & (b%2==0))
# print("True numbers only: ", b[(b>50) & (b%2==0)])

# # find all numbers which is not divisible by 7
# print(b[~(b%7 !=0)])


# broadcasting
print("================== Broadcasting =================")
# same shape
x = np.arange(6).reshape(2,3)
y = np.arange(6, 12).reshape(2,3)
print(x)
print(y)
print("same shape: ", x+y)
print()

# different shape
x1 = np.arange(6).reshape(2,3)
y1 = np.arange(3).reshape(1,3)
print(x1)
print(y1)
print("different shape: ", x1+y1)
print()