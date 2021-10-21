def get_file_data(filename='data.txt'):
    """Reads floating point CSV data from file and returns a list of lists

    keyword arguments:
    filename  --  string with file location
    """
    # open data.txt read-only
    # the file is CSV formatted, so split it by line and by field in line
    # open the file read-only
    # get a list of all the lines in the file and trim line-endings
    with open(filename, 'r') as my_data:
        lines = my_data.readlines()
        lines = [ line.rstrip('\n') for line in lines ]
    # that is all we need from the file, we can close it

    # these are comma separated lines -> split them into list of values
    # Finally, we need to convert text to numbers
    # (list comprehension can be nested)
    data = [ line.split(',') for line in lines] # list of lists
    data = [ [float(field) for field in row] for row in data ]
    return data

def get_row_sums(data=[]):
    """Returns a list of sums per row in a list of lists

    keyword arguments:
    data -- list of lists of floats
    """
    # rows are straight forward to summate: we just sum the line/list
    return [ sum(row) for row in data ]


def get_column_sums(data=[]):
    """Return a list of sums per column in a list of lists

    keyword arguments:
    data -- list of lists of floats
    """
    # Columns are harder. This functions:
    # loops over the column numbers based on the length of the first row
    # sums all fields with the same column number in all rows.
    # To do so, reset a variable sum_so_far to 0 for every new column number
    # Go over the rows, and add the value of the field to sum_so_far
    # finally, append that to the list of column_sums
    column_sums = []
    for colnr in range(len(data[0])):
        sum_so_far = 0
        for row in data:
            sum_so_far += row[colnr]
        column_sums.append(sum_so_far)
    return column_sums



my_data = get_file_data('data.txt') 
print(f"row sums: {get_row_sums(my_data)}")
print(f"colums sums: {get_column_sums(my_data)}")