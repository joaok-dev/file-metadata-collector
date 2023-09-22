import csv
import os
import sys
from datetime import datetime
from pprint import pprint

# Importing sys.argv for user input
user_input = sys.argv[1] if len(sys.argv) > 1 else os.curdir

# Get the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_script_directory)

# Define directory to scan and where to save the CSV
directory_path = user_input
save_directory = os.path.join(parent_directory, "data")
csv_filename = "metadata.csv"

# Construct the full save path

full_save_path = os.path.join(save_directory, csv_filename)

# Check if 'data' folder exists, if not, create it
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# List directory contents
directory_contents = os.listdir(directory_path)
pprint(f"Contents of directory {directory_path}: {directory_contents}")
print()

# Collect file metadata
all_file_metadata = []

for file in directory_contents:
    full_file_path = os.path.join(directory_path, file)  # Create the full path
    if os.path.isfile(full_file_path):  # Use the full path
        file_metadata = {
            "file_name": str(file),
            "file_size": os.stat(full_file_path).st_size,  # Use the full path
            "last_modified": datetime.fromtimestamp(
                os.stat(full_file_path).st_mtime
            ).strftime("%Y-%m-%d %H:%M:%S"),
        }
        all_file_metadata.append(file_metadata)


# Save metadata to CSV
with open(full_save_path, "w", newline="") as csvfile:
    csv_writer = csv.DictWriter(
        csvfile, fieldnames=["file_name", "file_size", "last_modified"]
    )
    csv_writer.writeheader()
    for metadata in all_file_metadata:
        csv_writer.writerow(metadata)
