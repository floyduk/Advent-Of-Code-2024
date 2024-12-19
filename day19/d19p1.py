# open and read the input file into a list of strings
input = open("day19/input.txt", "r").read().split("\n")
available_towels = [a.strip() for a in input[0].split(",")]
desired_patterns = input[2:]
longest_towel = max([len(a) for a in available_towels])

# Started off writing this recursive but then decided to use a queue
# instead for funsies. Then read part 2 and had to switch back to 
# recursive so I could use memoization.
# One little gotcha for me here - in the sample the longest towel is
# 3 stripes. Not so for part 2.
successful = 0
for pattern in desired_patterns:
    queue = set([pattern])
    while queue:
        p = queue.pop()
        if p in available_towels:
            # If the remaining pattern matches a towel then we're done
            successful += 1
            break
        else:
            # If not then check the first i chars in p for matching towels 
            # and if we find one then add the rest to the queue
            for i in range(1, min(longest_towel+1, len(p))):
                if p[:i] in available_towels: queue.add(p[i:])

print(f"Successful: {successful}")