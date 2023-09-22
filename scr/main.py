import csv
import os
from datetime import datetime

# Get the directory of the current script
current_script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_script_directory)

# Define directory to scan and where to save the CSV
directory_path = os.curdir
save_directory = os.path.join(parent_directory, "data")
csv_filename = "metadata.csv"

# Construct the full save path
full_save_path = os.path.join(save_directory, csv_filename)

# Check if 'data' folder exists, if not, create it
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# List directory contents
directory_contents = os.listdir(directory_path)
print(f"Contents of directory {directory_path}: {directory_contents}")
print()

# Collect file metadata
all_file_metadata = []

for file in directory_contents:
    if os.path.isfile(file):
        file_metadata = {
            "file_name": str(file),
            "file_size": os.stat(file).st_size,
            "last_modified": datetime.fromtimestamp(os.stat(file).st_mtime).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
        all_file_metadata.append(file_metadata)

# Output collected metadata to console
print(all_file_metadata)

# Save metadata to CSV
with open(full_save_path, "w", newline="") as csvfile:
    csv_writer = csv.DictWriter(
        csvfile, fieldnames=["file_name", "file_size", "last_modified"]
    )
    csv_writer.writeheader()
    for metadata in all_file_metadata:
        csv_writer.writerow(metadata)
