from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Hambre', 'Alfred']
sizes = [10, 90]
explode = (0, 0.2)  # only "explode" the 2nd slice (i.e. 'Hogs')
colors = ['red', 'lightblue']


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        colors=colors, startangle=90)
ax1.set_title('Razones por la que Gordo llora')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()