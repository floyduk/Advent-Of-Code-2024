# open and read the input file into a list of strings
input = open("day5/input.txt", "r").read().split("\n")

# Function to check the correctness of the page list order. 
# Returns true if page order is correct
def check_page_list_in_correct_order(page_list):
    for a in range(0, len(page_list)-1):
        for b in range(a+1, len(page_list)):
            if [page_list[b], page_list[a]] in rules:
                return(False)
    return(True)

# Variables we'll use to store the rules and page lists
rules = []
pages = []

########
# MAIN #
########

# Import the rules and pages lists from the puzzle input file
importing_rules = True
for line in input:
    if line == "":
        importing_rules = False
    else:
        if importing_rules:
            rules.append([int(a) for a in line.split("|")])
        else:
            pages.append([int(a) for a in line.split(",")])


# Iterate the list of page_lists checking each one for correctness
# When a correct one is found then add the middle value in the list
# to the total.
total_of_middle_values = 0
for page_list in pages:
    if check_page_list_in_correct_order(page_list):
        total_of_middle_values += page_list[len(page_list)//2]

print(f"Total: {total_of_middle_values}")