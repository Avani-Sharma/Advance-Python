# Pandas : is a python library which is used to manipulate the data (data manipulation)
# and for the data analysis
# data types in pandas: 1: series and 2: dataframe 

# install library pandas:------ pip install pandas

# importing pandas
import pandas as pd
import numpy as np
arr = np.array([1,2,3,4])
# 1: series in pandas: it is a data type in pandas which is having one dimension and each of the 
# elements have the labels that is known as series.
# we can create series by list or numpy array 
# no. of elements = no. of index if it is not equal it will give an value error 
a = pd.Series(arr, index=['first', 'second', 'third', 'fourth'])
print(a)

# indexing
print(a['first'])

# vectorization is possible
print(a+10)

