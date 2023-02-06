import hashlib
import os
import sys
import time

def hash_file(filename):
    """Return the SHA-256 hash of the contents of a file."""
    hasher = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def hash_directory(path):
    """Return the SHA-256 hash of the contents of all files in a directory."""
    hasher = hashlib.sha256()
    for root, _, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    hasher.update(data)
    return hasher.hexdigest()

# Ask the user for the paths of the two directories
dir1_path = input("Enter the path of the first directory: ")
dir2_path = input("Enter the path of the second directory: ")

# Display a loading animation while hashing the contents of the directories
print("Hashing the contents of the directories...")
for i in range(10):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.2)

# Hash the contents of the two directories
dir1_hash = hash_directory(dir1_path)
dir2_hash = hash_directory(dir2_path)

# Compare the hashes and print the result
if dir1_hash == dir2_hash:
    result = "HASH RESULT SAME"
else:
    result = "HASH RESULT NOT SAME"
print("\nHash of first directory:", dir1_hash)
print("Hash of second directory:", dir2_hash)
print(result)
