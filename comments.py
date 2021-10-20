# open data.txt read-only
# the file is CSV formatted, so split it by line and by field in line
# The goal is to loop over the data and calculate sums
# one list of sums for the rows
# one list of sums for the columns

# open the file read-only
# get a list of all the lines in the file and trim line-endings
with open('data.txt', 'r') as my_data:
    lines = my_data.readlines()
    lines = [ line.rstrip('\n') for line in lines ]
# that is all we need from the file, we can close it

# these are comma separated lines -> split them into list of values
# Finally, we need to convert text to numbers
# (list comprehension can be nested)
data = [ line.split(',') for line in lines] # list of lists
data = [ [float(field) for field in row] for row in data ]

# rows are straight forward to summate: we just sum the line/list
row_sums = [sum(row) for row in data]

# Columns are harder. The idea is:
# loop over every field in line 1 and remember the column number
# summate all field with the same column number in all other rows.
# To do so, reset a variable sum_so_far to 0 for every new column number
# Go over the lines, and add the value of the field to sum_so_far
# finally, append that to the list of column_sums
column_sums = []
for colnr in range(len(data[0])):
    sum_so_far = 0
    for row in data:
        sum_so_far += row[colnr]
    column_sums.append(sum_so_far)


print(f"row sums: {row_sums}")
print(f"columns sums: {column_sums}")