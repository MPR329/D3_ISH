import os
import json


# Get the file size in bytes
file_path = 'combined_data.json'
# Load the JSON file and get the length of the structure
with open(file_path, 'r') as file:
    data = json.load(file)

if isinstance(data, list):
    length = len(data)  # Number of elements in the array
elif isinstance(data, dict):
    length = len(data.keys())  # Number of keys in the dictionary

print("Length of the JSON structure:", length)