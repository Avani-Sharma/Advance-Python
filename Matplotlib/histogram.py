import matplotlib.pyplot as plt
# histogram: is a type of plot which is used to show the relationship between two variables.
# ex: distribution of ages, distribution of income etc.
# whenever we have to find the distribution of partition of each of class or labels  then we use histogram.
# creating data
ages = [22, 25, 27, 30, 35, 40, 45, 50, 55, 60]
# creating a histogram
plt.hist(ages, bins=5, color='blue', edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

