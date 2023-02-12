# 811 Helper
A helper program to organize and chart 811 emergency ticket data.
It will work in any state that uses managetickets.com for 811 data.

This program was built to organize 811 data from managetickets.com into graphs, for easy visualization of emergency ticket numbers. It is designed with some hardcoded strings for dealing with emergencies, but this could be forked to deal with a different use-case. 
USAGE:
text_to_csv.py
Run your query on managetickets.com to get the data you want to use, copy the raw data into a text file and save. Run text_to_csv.py against the file with the raw copied data to get a file that is organized in comma separated value format. Note that your original text file must have the data organzied by TABS, not spaces, just as is copied from managetickets.com

graph.py
Run graph.py with your .csv file you created to turn your .csv data into a graph, which saves as a .png image file.
