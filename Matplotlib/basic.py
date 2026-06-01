# matplotlib: is data visualization library which is used to visualize the data in the form of graphs and charts. 
# ex: line plot, bar plot, histogram, pie chart etc. 
import matplotlib.pyplot as plt

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