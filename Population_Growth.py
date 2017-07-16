# Program utilizing the pandas and matplotlib.pyplot to create pivot tables and plots for panel data on countries' population's over time

import pandas as pd
import matplotlib.pyplot as plt

# Read csv data from computer
pop_df = pd.read_csv('C:/Users/Dennzy/Desktop/Development And Growth 582/HW1/population.csv')
# Create pivot table from the data with values being the Population indexing by year and the variable being each different country
pop_df = pop_df.pivot_table(values='Population', index='Year', columns='Country')
# Manipulate dataframe by stacking countries by year
stacked = pop_df.stack()
# Create line plot with a legend for each country with population on the vertical axis and the year on the horizontal axis
pop_df['USA'].plot(legend=True)
pop_df['CAN'].plot(legend=True)
pop_df['MEX'].plot(legend=True)
# Add a label to the y axis and title
plt.ylabel('Population in millions')
plt.title('Population growth of North American countries over time')

