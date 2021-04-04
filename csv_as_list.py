# author: github.com/teo113
# desc: This script reads in a csv file/column as a list.

import csv

csv_file = r'data/list.csv'

# pass each row of csv as a list
with open(f'{csv_file}', newline='') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header row
    data = list(reader)

print(data)


# pass each value found in a chosen column as a list
col_list = []
with open(f'{csv_file}', newline='') as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header row
    for row in csv.reader(f):
        col_list.append(row[1])

print(col_list)

# use pandas to pass a chosen column as a list
