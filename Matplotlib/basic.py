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
