# open and read the input file into a list of strings
input = open("day1/input.txt", "r").read().split("\n")

# Read in the lists creating a left list and a right list
left_list = []
right_list = []
for line in input:
    pieces = line.split()
    left_list.append(int(pieces[0]))
    right_list.append(int(pieces[1]))

# Calculate the similarity score
similarity_score = 0
for number in left_list:
    similarity_score += (number * right_list.count(number))

print(f"Similarity Score: {similarity_score}")