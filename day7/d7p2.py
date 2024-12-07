# Recursive function that goes pairwise through the list first adding then 
# multiplying and then if there are more values still on the list recursively 
# calling itself to do the same for the next pair. When we're down to the last
# pair of numbers we check if our operations generate the desired result and
# pass True or False back up the chain to the caller.
def try_operators(result, operands):
    # Generate the sum, product and concatenation of the first 2 operands
    s = operands[0] + operands[1]
    p = operands[0] * operands[1]
    c = int(str(operands[0]) + str(operands[1]))

    # One very small shortcut suggested by @Cyphase. These operators can only 
    # increase the result so we can quit trying if we've already exceeded result
    if s > result and p > result and c > result: return(False)

    # Once we're on the last 2 operands we compare with the result
    if len(operands) == 2:
        if s == result or p == result or c == result: return(True)
    else:
        # If we're not on the last 2 operands then call again with the first 2
        # operands removed and our sum, product or concatenation inserted in front
        if try_operators(result, [s] + operands[2:]):
            return(True)
        elif try_operators(result, [p] + operands[2:]):
            return(True)
        elif try_operators(result, [c] + operands[2:]):
            return(True)
        else:
            return(False)

########
# MAIN #
########

# open and read the input file into a list of strings
input = open("day7/input.txt", "r").read().split("\n")

# Iterate through the input grabbing the values we need and then passing them to the
# recursive function to test if they produce the desired result. If they do then add
# the result to our running total.
total = 0
for line in input:
    result, rest = line.split(":")
    result = int(result)
    operands = [int(a) for a in rest.split()]
    if try_operators(result, operands):
        total += result

print(f"Total of successful rows: {total}")
