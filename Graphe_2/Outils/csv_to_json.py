import pandas as pd

# Load the CSV file
file_path = 'match_info.csv'
df = pd.read_csv(file_path)

# Convert the dataframe to a JSON string
json_data = df.to_json(orient='records')

# Save the JSON string to a file
json_file_path = 'matches_info.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

json_file_path
