import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
# scatter plot: is a type of plot which is used to show the relationship between two variables.
# ex: height vs weight, age vs income etc.
# whenever there is two numerical column and we have to find the data that how they're
# actually spread then we can use scatter plot to show the relationship between them.
# 1. independent variable (x-axis)
house_size_sqft = [1500, 2000, 2500, 3000, 3500]
# 2. dependent variable (y-axis)
house_price = [300000, 400000, 500000, 600000, 700000]
# categorical variable 
num_bedrooms = [3, 4, 4, 5, 5]
plt.figure(figsize=(8, 5))
plt.scatter(house_size_sqft, house_price)
plt.scatter(house_size_sqft, num_bedrooms, color='red')
plt.title('House Size vs Price and Number of Bedrooms')
plt.show()