import pandas as pd

# Read CSV file and store value into data frame variable
company_df = pd.read_csv("company_data.csv", sep=",")
# print(company_df)

# Convert pands data frame to JSON
output_data = company_df.to_json("final_data.json", indent=1, orient='records')
print('File created successfully')