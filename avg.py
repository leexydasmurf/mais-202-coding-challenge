import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#import csv file using pandas 
#change this path depending on from where you are running it
df = pd.read_csv("E:\CODE\PYTHON\data.csv")

#new dataframe with only the purpose and the interest rate columns
purposedf = df[['purpose', 'int_rate']]

#mean grouped by each category
avg_int = purposedf.groupby('purpose')['int_rate'].mean().reset_index()

#rename the column to display avg_rate instead of int_rate
avg_int.columns = ['purpose','avg_rate']
print(avg_int)

#plot the dataframe using pandas
#make adjustments to the font, size, title, and colors
ax = avg_int.plot(
    avg_int['purpose'],
    kind='bar',
    legend=False,
    fontsize=7,
    rot=0, 
    title ="Mean interest rate by loan purpose", 
    color=[plt.cm.Paired(np.arange(len(avg_int)))])

#turn on grid, change color, set it to background and label each axis
ax.grid('on', which='major', axis='y', color='white')
ax.set_facecolor('lavender')
ax.set_axisbelow(True)
ax.set_xlabel("purpose")
ax.set_ylabel("mean(int_rate)")

#show the graph using pyplot
plt.show()