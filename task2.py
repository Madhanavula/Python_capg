import os
# Initialize variables to keep track of the folder with maximum size
max_folder = ""
max_size = 0

c_drive_path = r"C:\python"

# Iterate through all directories and files in the C drive
for root, dirs, files in os.walk(c_drive_path):
    folder_size = 0
    for file in files:
        file_path = os.path.join(root, file)
        try:
            folder_size += os.path.getsize(file_path)
        except (FileNotFoundError, PermissionError, OSError) as e:
            print(f"Error: {e} - Skipping file {file_path}")

    # Check if the current folder's size is larger than the current maximum
    if folder_size > max_size:
        max_size = folder_size
        max_folder = root

# Print the folder with the maximum size and its size in bytes
print(f"The folder taking the maximum space on C drive is: {max_folder}")
print(f"Size: {max_size} bytes")
