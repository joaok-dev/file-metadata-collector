import csv
import os
import sys
from datetime import datetime
from pprint import pprint

# Import sys.argv to read the directory path from the command-line arguments
user_input = (
    sys.argv[1] if len(sys.argv) > 1 else os.curdir
)  # Default to the current directory if no input is given

# Get the directory where this script resides
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the script's directory
parent_directory = os.path.dirname(current_script_directory)

# Define the directory to scan and where to save the CSV file
directory_path = user_input
save_directory = os.path.join(parent_directory, "data")
csv_filename = "metadata.csv"

# Construct the full path where the CSV will be saved
full_save_path = os.path.join(save_directory, csv_filename)

# Check if the 'data' folder exists; if not, create it
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Check if the provided path is a directory
if not os.path.isdir(directory_path):
    print(f"Error: The provided path '{directory_path}' is not a directory.")
    sys.exit(1)

# List the contents of the directory
directory_contents = os.listdir(directory_path)
pprint(f"Contents of directory {directory_path}: {directory_contents}")
print()

# Initialize list to store file metadata
all_file_metadata = []

# Loop through each file in the directory
for file in directory_contents:
    full_file_path = os.path.join(directory_path, file)
    try:
        # Check if it's a file and not a directory
        if os.path.isfile(full_file_path):
            # Get the file's metadata using os.stat
            file_stat = os.stat(full_file_path)
            file_metadata = {
                "file_name": str(file),
                "file_size": file_stat.st_size,
                "last_modified": datetime.fromtimestamp(file_stat.st_mtime).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
            }
            all_file_metadata.append(file_metadata)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File '{full_file_path}' not found.")
        continue

# Save the collected metadata to a CSV file
with open(full_save_path, "w", newline="") as csvfile:
    csv_writer = csv.DictWriter(
        csvfile, fieldnames=["file_name", "file_size", "last_modified"]
    )
    csv_writer.writeheader()  # Write the header row
    for metadata in all_file_metadata:
        csv_writer.writerow(metadata)  # Write each row of metadata
