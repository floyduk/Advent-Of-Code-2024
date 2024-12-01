# open and read the input file into a list of strings
input = open("day1/input.txt", "r").read().split("\n")

# Read in the lists creating a left list and a right list
left_list = []
right_list = []
for line in input:
    pieces = line.split()
    left_list.append(int(pieces[0]))
    right_list.append(int(pieces[1]))

# Sort the lists
left_list.sort()
right_list.sort()

# Calculate the distances between the lists and add them as we go
total_distance = 0
for i in range(0,len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(f"Total distance: {total_distance}")