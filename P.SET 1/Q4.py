import os

# Specify the directory path
path = r"c:/"

# Get the contents of the directory
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)