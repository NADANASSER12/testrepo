import os
import re

def rename_files(directory, replace_char='_'):
    special_chars = r'[&%*?:/\\<>|" ]|\%20'
    for root, _, files in os.walk(directory):
        for filename in files:
            if re.search(special_chars, filename):
                new_filename = re.sub(special_chars, replace_char, filename)
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")


rename_files('D:\3d\My dataset\data\models')