# open and read the input file into a list of strings
input = open("day2/input.txt", "r").read().split("\n")

# Check if the supplied row can be considered safe according
# to the rules about going up or down in increments of between
# 1 and 3.
def row_is_safe(row):
    direction = "up" if row[0] < row[1] else "down"
    lastval = row[1]
    if not(0 < abs(row[0] - row[1]) <= 3):
        return(False)

    for i in range(2, len(row)):
        if not(0 < abs(lastval - row[i]) <= 3):
            return(False)
        if direction == "up" and row[i] < lastval:
            return(False)
        if direction == "down" and row[i] > lastval:
            return(False)
        lastval = row[i]
    
    return(True)

########
# MAIN #
########

# Iterate the rows counting the number of safe rows
count_safe_rows = 0
for line in input:
    row = [int(a) for a in line.split()]
    count_safe_rows += 1 if row_is_safe(row) else 0

print(f"Safe rows: {count_safe_rows}")