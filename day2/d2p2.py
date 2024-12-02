# open and read the input file into a list of strings
input = open("day2/input.txt", "r").read().split("\n")

# Simple function implements the rules about values going up or down
# by between 1 and 3. Returns true if the pair matches the direction and
# is in the necessary range.
def is_safe(dir,a,b):
    if not(0 < abs(a - b) <= 3):
        return(False)
    if dir == "up" and a >= b:
        return(False)
    if dir == "down" and a <= b:
        return(False)
    return(True)

# This code will allow a single value to be skipped 
# but it doesn't handle the first or second value being skipped.
# It's a bit hacky but I call this function first with the full list
# and no initial skipped value. And then I call it again with the first
# item in the list removed. And then again with the second removed. 
# Those times I supply an initial skipped value of 1 so that no more 
# values are allowed to be skipped here
def row_is_safe(row, skipped = 0):
    direction = "up" if row[0] < row[1] else "down"
    lastval = row[0]

    for i in range(1, len(row)):
        if skipped > 1:
            return(False)
        
        if is_safe(direction, lastval, row[i]):
            lastval = row[i]
        elif (i+1 < len(row)) and is_safe(direction, lastval, row[i+1]):
            skipped += 1
        elif (i+1 >= len(row)) and skipped == 0:
            skipped += 1
        else:    
            return(False)

    if skipped > 1:
        return(False)
    return(True)

########
# MAIN #
########

# Iterate the rows counting the number of safe rows
count_safe_rows = 0
for line in input:
    # Split the row into values and convert the values to int
    row = [int(a) for a in line.split()]

    # Check if this row is considered safe by using the row_is_safe() function
    # as described in the function header
    if row_is_safe(row):
        count_safe_rows += 1
    elif row_is_safe(row[1:], 1): # Check without row index 0
        count_safe_rows += 1
    elif row_is_safe(row[:1] + row[2:], 1): # Check without row index 1
        count_safe_rows += 1

print(f"Safe rows: {count_safe_rows}")