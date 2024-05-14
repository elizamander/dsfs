import numpy as np
from matplotlib import pyplot as plt
from collections import Counter


friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Create a figure and an axes.
fig, ax4 = plt.subplots()

# Plotting the data
ax4.scatter(friends, minutes)

# Label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    ax4.annotate(label,
                xy=(friend_count, minute_count),  # Position of label
                xytext=(5, -5),                  # Slightly offset from the actual point
                textcoords='offset points')

# Setting the title and labels
ax4.set_title("Daily Minutes vs. Number of Friends")
ax4.set_xlabel("# of friends")
ax4.set_ylabel("daily minutes spent on the site")

plt.show()