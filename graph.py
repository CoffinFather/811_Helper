#!/usr/bin/env python3
# This script takes a .csv file and turns it into a bar graph.
# It is being used for to show the number of emergencies called into the 811 system by specific contractors
# so the labels and counts strings are hardcoded for this purpose.
import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the csv file
filename = input("Please enter the .csv filename: ")
if os.path.isfile(filename):
	df = pd.read_csv(filename)
else:
	print("File not found")
	exit()


# Count the occurrences of each Excavator Company
counts = df['Excavator Company'].value_counts()

# Filter the counts to only include excavator companies that occur 5 or more times
counts = counts[counts >= 5]

# Sort the values by number of occurrences
counts = counts.sort_values(ascending=True)

# Create a horizontal bar graph
counts.plot(kind='barh', color='#86bf91', zorder=2, width=0.85)
ax = plt.gca()

# Add the count value next to the corresponding bar
for i, v in enumerate(counts.values):
    ax.text(v, i, str(v), color='black', fontweight='bold')

# Set the title and labels
title = input("Please enter the title of the graph: ")
plt.title(title)
plt.xlabel("Number of Emergencies")
plt.ylabel("Excavator Company")
plt.tight_layout()

# Show the plot
plt.show()
