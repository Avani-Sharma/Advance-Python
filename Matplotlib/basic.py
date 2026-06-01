# matplotlib: is data visualization library which is used to visualize the data in the form of graphs and charts. 
# ex: line plot, bar plot, histogram, pie chart etc. 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# line plot: is a type of plot which is used to show the relationship between two variables.
# ex: stock price over time, temperature over time etc. 
# creating data
x = [1, 2, 3, 4, 5]
y = [10,20,30,40,50]
# creating a line plot
plt.plot(x, y)
# adding title and labels
plt.title('Line Plot')
plt.xlabel('days')
plt.ylabel('price')
# displaying the plot
plt.show()
# creating a figure with specific size
plt.figure(figsize=(8, 4))
# to customize the line plot with color and marker and linestyle
plt.plot(x, y, color='red', marker='o', linestyle='--')


# another example of line plot with multiple lines
# Timeline (x-axis sharing)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'june']
# performance data for three different lines(y-axis)
online_sales = [100, 150, 200, 250, 300, 350]
retail_sales = [80, 120, 160, 200, 240, 280]
wholesale_sales = [180, 270, 360, 450, 540, 630]
# creating a line plot with multiple lines
plt.plot(months, online_sales, label='Online Sales', marker='o', color='blue')
plt.plot(months, retail_sales, label='Retail Sales', marker='s', color='green')    
plt.plot(months, wholesale_sales, label='Wholesale Sales', marker='^', color='red')
plt.title('Sales Performance Over Time')
plt.xlabel('Months')
plt.ylabel('Sales')
# adding legend to differentiate between the lines
plt.legend()
plt.show()



# another example
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10
y1 = np.cos (x)  # cosine wave
plt.plot(x, y1, label='Cosine Wave', color='purple')
plt.title('Cosine Wave')
plt.show()



# bar plot: is a type of plot which is used to show the relationship between two variables.
# ex: sales by category, population by country etc.
# another example
data = {
    'genre': ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'],
    'units_sold': [150, 200, 250, 100, 300]
}
df = pd.DataFrame(data)
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.plot(df['genre'], df['units_sold'], marker='o', color=colors)
plt.title('Units Sold by Genre')
plt.show()




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