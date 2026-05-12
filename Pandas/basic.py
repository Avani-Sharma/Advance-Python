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
# to check datatype
print(a.dtype)

print()

# 2: data frame: a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure
# it as a Python version of an Excel spreadsheet or a SQL table
data = {
    'Name': ['avani', 'chinki'],
    'Marks': [20, np.nan],
    'location': ['Jaipur', 'Delhi']
}
print(data)
b = pd.DataFrame(data, index=['first_stud', 'second_stud'])
print(b)
print(b['location'])

# to perform any string operations on the object data type column we use .str -> any function
# to add any new column into the dataframe then we use 
# dataframe_name[new_column] = new_value
b['Upper_letter'] = b['location'].str.upper()
print(b['Upper_letter'])
print()
# to add new col
b['new_col'] = 0
print(b['new_col'])
print()
# to find max
print(b['Marks'].max())
# to check any null value from the series (np.nan)
# b['col].isna(): --- this returns the boolean value
# if the entry is true === then it means there is null value present
# if the entry is false === then there is not null is present 
print(b['Marks'].isna().sum())

print()

# ques1: 
# create a data frame using dict 
# ex: employee: emp_name, salary, year of experience, increment
# atleast have one or more than null value in each of the col 
# first check the data type of if the column separately
# check the highest salary if the person 
# median salary
# mode of the salary
# how many people are at the same experience
# check each of the col which has how many null values (null value count)

employee = {
    'Name': ['avani', 'chinki', 'himani', 'pihu', 'urvashi'],
    'salary': [3000, np.nan, 1500, np.nan, 2000],
    'YOE': [2, 3, 1, 4, 2],
    'increment': [400, 300, 500, 200, 400]
}
print(employee)
emp = pd.DataFrame(employee)
print(emp)
# data types of each column
print(emp.dtypes)
# highest salary
print(emp['salary'].max())
# median salary
print(emp['salary'].median())
# mode of salary
print(emp['salary'].mode())
# same experience
print(emp['YOE'].value_counts())
# null values
print(emp.isnull().sum())

