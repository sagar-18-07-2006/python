#write a python program to print contnets of a directory using the os module
import os

# Specify the directory you want to list
directory_path = "/Users/Asus"  # current directory, or you can replace with any path

# List all files and directories in the specified path
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
