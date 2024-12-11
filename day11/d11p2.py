from functools import cache

# open and read the input file into a list of strings
input = [int(a) for a in open("day11/input.txt", "r").read().split()]

# Recursive function that given a number and a required blink count will return 
# the number of stones it produces. For large blink counts this is only possible 
# due to the @cache instruction which makes a cache of arguments and results so
# that if we see arguments we've seen before then we know the result already.
@cache
def blink(num, blinks):
    if blinks == 0:
        # No more blinks are required
        return(1)
    elif num == 0:
        # Number is 0, return 1 and recurse down with 1 fewer required blinks
        return(blink(1, blinks-1))
    elif len(str(num))%2 == 0:
        # Number has an even number of digits. Recurse down 2 paths, one for
        # the first half and the other for the second.
        numstr = str(num)
        l = len(numstr)//2
        return(blink(int(numstr[:l]), blinks-1) + blink(int(numstr[-l:]), blinks-1))
    else:
        # Otherwise multiply by 2024. Recurse down with num * 2024 and 1 fewer
        # required blinks
        return(blink(num * 2024, blinks-1))

########
# MAIN #
########

# Iterate the list of numbers calling blink() which returns a resulting number
# of stones and sum the total.
total = 0
for a in input:
    total += blink(a, 75)

print(f"Total: {total}")
