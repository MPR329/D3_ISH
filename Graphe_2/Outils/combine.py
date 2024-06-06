import os
import json

def combine_json_files(folder_path):
    combined_data = []

    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file
    for file_name in files:
        if file_name.endswith('.txt'):  # Check if it's a TXT file
            # Extract the file identifier from the file name
            file_identifier = file_name.split('_')[0]
            file_path = os.path.join(folder_path, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    # Add file identifier to each JSON object
                    for obj in data:
                        obj['file_identifier'] = file_identifier
                    combined_data.extend(data)
                    print(f"Loaded {file_name}")
            except Exception as e:
                print(f"Error loading {file_name}: {e}")

    return combined_data

def save_combined_data(combined_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(combined_data, file, indent=4)
    print(f"Combined data saved to {output_file}")

# Example usage:
folder_path = 'SCRAPED_DATA_ONLY'
output_file = 'combined_data.json'

combined_data = combine_json_files(folder_path)

save_combined_data(combined_data, output_file)
