# display info from 'activity.csv'
# ingore the missing values (NA) in the dataset
# 1. Calculate the total number of steps taken p/d
# 2. Make a histogram of the total number of steps taken each day
# 3. Calculate and report the mean and median of the total number of steps taken p/d

import csv, pygal, statistics
from datetime import datetime

with open('activity.csv') as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)
    dates = {}
    d = 0

    for row in reader:
        if row[0] == 'NA': # checks for missing values in steps column: row[0]
            continue # skips the missing values
        else:
            dates.setdefault(row[1], [1])
            dates[row[1]].append(int(row[0]))

total_steps = [] # list to append the total steps p/d
for value in dates.values():
     total_steps.append(sum(value))

hg = pygal.Bar()
hg.title = 'Steps p/d'
hg.x_labels = dates
hg.x_title = 'Dates'
hg.y_title = 'Frequency'
hg.add('date', total_steps)
hg.render_to_file('histogram.svg')

print(f'Total steps: {total_steps}')
# using statistics library to calculate mean and median
print(f'MEAN: {str(statistics.mean(total_steps))} p/d')
print(f'MEDIAN: {str(statistics.median(total_steps))} p/d')