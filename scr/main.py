import os
from datetime import datetime

directory_path = os.curdir
directory_contents = os.listdir(directory_path)

print(f"Contents of directory {directory_path}: {directory_contents}")
print()


for file in directory_contents:
    if os.path.isfile(file):
        file_path = os.path.join(directory_path, file)
        file_metadata = os.stat(directory_path)

        file_name = str(file)
        file_size = file_metadata.st_size
        file_last_modification = datetime.fromtimestamp(
            file_metadata.st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S")

        print(f"{file_name} - Size: {file_size} bytes")
        print(f"Last Modified: {file_last_modification}")
