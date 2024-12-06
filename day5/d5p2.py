from functools import cmp_to_key

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

# This is an old style comparator sort function. I used cmp_to_key()
# to turn this into a newer style key sort function when sorting an
# incorrectly ordered page_list.
def my_sort(a, b):
    global rules
    if [a, b] in rules:
        return -1
    elif [b, a] in rules: 
        return 1
    else:
        return 0

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
# When an incorrect one is found I use the built-in sorted() function
# to sort the list using the comparator sort function my_sort above
# and then pull out and sum the middle number from the sorted list.
total_of_middle_values = 0
for page_list in pages:
    if not check_page_list_in_correct_order(page_list):
        sorted_page_list = sorted(page_list, key=cmp_to_key(my_sort))
        print(f"{sorted_page_list}")
        total_of_middle_values += sorted_page_list[len(sorted_page_list)//2]

print(f"Total: {total_of_middle_values}")