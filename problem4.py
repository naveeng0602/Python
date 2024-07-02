import os

# Get the directory path (replace 'path/to/your/directory' with the actual path)
directory_path = "/"

# Use os.listdir() to get a list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of", directory_path)
for item in contents:
  print(item)
