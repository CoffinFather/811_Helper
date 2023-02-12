#!/usr/bin/env python3
# This script turns the data from a .txt file into a .csv file
# The data in your .txt file should be tabbed not spaced. The purpose of the script is to organize raw data from the 811 system
# so the column name strings are hardcoded for this purpose.

import csv
import os

data = ""
filename = input("Please enter the name of the file you want to use: ")

if not os.path.exists(filename):
    print(f"{filename} does not exist.")
    exit()
else:
    with open(filename, 'r') as file:
        data = file.read()


# Split the data into lines
lines = data.strip().split("\n")

# Ask the user for the filename
filename = input("Enter the filename to save as: ")
if not filename:
	print("File not saved.")
	exit()

# Open the file in write mode
with open(filename, 'w', newline='') as f:
    # Create a CSV writer
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    # Write the column names
    writer.writerow(["Ticket#", "Type", "Call Date", "Excavator Company", "Addr", "Street", "City"])

    # Iterate over the lines
    for line in lines:
        # Split the line into fields
        fields = line.split("\t")

        # Write the fields to the CSV file
        writer.writerow(fields)
