# Read the input data and split it into a list of strings
data = input().split()

# Initialize a list to store the commands
commands = []

# Read commands until "3:1" is encountered
while True:
    command = input()
    if command == "3:1":
        break
    commands.append(command)

# Process each command
for cmd in commands:
    parts = cmd.split()
    action = parts[0]

    if action == "merge":
        start, end = map(int, parts[1:3])
        # Merge elements from start to end
        data[start:end + 1] = [''.join(data[start:end + 1])]
    elif action == "divide":
        index, partitions = map(int, parts[1:3])
        # Divide the element at index into partitions
        element = data[index]
        partition_length = len(element) // partitions
        divided_parts = [element[i:i + partition_length] for i in range(0, len(element), partition_length)]
        data.pop(index)
        data[index:index+1] = divided_parts

# Print the result by joining the data with spaces
result = ' '.join(data)
print(result)
