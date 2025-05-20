# Write a python code for the convert csv file to json and json to csv
import pandas as pd
import json

# function for convert CSV to JSON
def csvToJson(file_name):
    df = pd.read_csv(file_name)
    # result_dict = dict(zip(df['Enrollment Number'], df['Student Name']))
    # # Convert the dictionary to JSON
    result_dict = df.to_json()
    # result_json = json.dumps(result_dict)

    return result_dict

print(csvToJson("Book1.csv"))



# JSON string
json_data = {
  "Enrollment Number": {
    "0": "ENR20250101",
    "1": "ENR20250102",
    "2": "ENR20250103",
    "3": "ENR20250104",
    "4": "ENR20250105",
    "5": "ENR20250106",
    "6": "ENR20250107",
    "7": "ENR20250108",
    "8": "ENR20250109",
    "9": "ENR20250110"
  },
  "Student Name": {
    "0": "Aarav Mehta",
    "1": "Priya Sharma",
    "2": "Rohan Verma",
    "3": "Ananya Kapoor",
    "4": "Devansh Singh",
    "5": "Meera Joshi",
    "6": "Kunal Deshmukh",
    "7": "Ishita Nair",
    "8": "Tanishq Bhatt",
    "9": "Sneha Reddy"
  }
}

# Convert the nested dict to a DataFrame
df = pd.DataFrame(json_data)
print(df)

# Transpose it so keys become rows
df = df.transpose()
df = df.rename_axis('Field').reset_index()

# Convert column-wise JSON to row-wise DataFrame
df = pd.DataFrame(json_data).T
df = df.rename_axis(index=None, columns=None).T.reset_index(drop=True)

# Save to CSV
df.to_csv("students.csv", index=False)

print("CSV file 'students.csv' created successfully.")
