# open and read the input file into a single string
input = open("day9/input.txt", "r").read()

# We will start out with a list of files and spaces and then as we defrag we'll remove 
# from both files and spaces and append to moved_files
files = []
spaces = []
moved_files = []

# iterate the chars in the string and create from it a list of files and a list of spaces
# keeping track of the block number and file_id as we go
block = 0
is_file = True
file_id = 0
for c in input:
    size = int(c)
    if is_file:
        if size > 0:
            files.append((block, size, file_id))
            file_id += 1
    else:
        if size > 0:
            spaces.append((block, size))
    block += size
    is_file = not is_file

# Iterate through the list of spaces filling them up using files from the end of the drive
while len(files):
    # Grab data about the last file
    (last_file_start, last_file_size, last_file_id) = files[-1]

    # Search for the first space that can hold the last file
    found = False
    for i in range(0, len(spaces)):
        if spaces[i][0] >= last_file_start:
            # Files should ONLY move left, not right. So if this space is to the right of the file
            # then we should stop searching
            break
        elif spaces[i][1] > last_file_size:
            # Found a space bigger than I need
            print(f"Moving {last_file_id} from {last_file_start} to {spaces[i][0]} and adjusting space remaining")
            moved_files.append((spaces[i][0], last_file_size, last_file_id))
            spaces[i] = (spaces[i][0] + last_file_size, spaces[i][1] - last_file_size)
            found = True
            break
        elif spaces[i][1] == last_file_size:
            # Found a space the exact size I need
            print(f"Moving {last_file_id} from {last_file_start} to {spaces[i][0]}")
            moved_files.append((spaces[i][0], last_file_size, last_file_id))
            del spaces[i]
            found = True
            break

    if not found:
        # If we didn't find a space big enough just move this file to the moved_files list
        print(f"Not moving {last_file_id}")
        moved_files.append(files[-1])

    # We've dealt with this file so delete it from the list
    del files[-1]

# Calculate the checksum by summing the products of block number and file ID
checksum = 0
for file in moved_files:
    for i in range(file[0], file[0] + file[1]):
        checksum += file[2] * i

print(f"Checksum: {checksum}")
