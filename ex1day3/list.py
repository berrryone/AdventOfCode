import re

# Load the data from the file
with open('text.txt', 'r') as file:
    data = file.read()

# Regular expression to match valid mul(X,Y) instructions
mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')

# Initialize a variable to hold the sum of results
total_sum = 0

# Find all matches of the pattern in the data
matches = mul_pattern.findall(data)

# For each match, compute the multiplication and add to the total sum
for match in matches:
    X, Y = int(match[0]), int(match[1])
    total_sum += X * Y

# Output the result
print(f"Total sum of products: {total_sum}")
