import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# bar plot: is a type of plot which is used to show the relationship between two variables.
# ex: sales by category, population by country etc.
# another example
data = {
    'genre': ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'],
    'units_sold': [150, 200, 250, 100, 300]
}
df = pd.DataFrame(data)
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.bar(df['genre'], df['units_sold'], color='blue')
plt.title('Units Sold by Genre')
plt.show()