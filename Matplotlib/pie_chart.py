import matplotlib.pyplot as plt
# pie chart: is a type of plot which is used to show the relationship between two variables.
# ex: sales by category, population by country etc.
# whenever we have to find the distribution of partition of each of class or labels  then we use pie chart.
# creating data
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [20, 30, 25, 15, 10]
explode = (0.1, 0, 0, 0, 0)  # explode the first slice (A)
# creating a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title('Distribution of Categories')
plt.show()