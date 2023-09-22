import os
from datetime import datetime

directory_path = os.curdir
directory_contents = os.listdir(directory_path)

print(f"Contents of directory {directory_path}: {directory_contents}")
print()

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

print(all_file_metadata)
