# open and read the input file into a list of strings
input = open("day11/input.txt", "r").read().split()

# A simple function to apply the blink rules. Give it a number 
# and it will return 1 or 2 numbers.
def apply_rules(numstr):
    result = list()

    if numstr == "0":
        # Number is 0
        return(["1"])
    elif len(numstr)%2 == 0:
        # Number has an even number of digits
        l = len(numstr)//2
        left = numstr[:l]
        right = numstr[-l:].lstrip("0")
        if right == "": right = "0"
        return([left, right])
    else:
        return([str(int(numstr) * 2024)])

########
# MAIN #
########

# This is very much the brute force approach. Iterate the numbers in
# the input blinking 25 times for each number. Count the size of the 
# resulting list and then move onto the next number. It works for 25
# blinks. Not so much for part 2.
total = 0
for a in input:
    numlist = [a]
    next_numlist = []
    for i in range(0, 25):
        for n in numlist:
            next_numlist += apply_rules(n)
        numlist = next_numlist
        next_numlist = []
    total += len(numlist)
    
print(total)
