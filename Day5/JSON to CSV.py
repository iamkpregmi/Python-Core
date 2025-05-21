import pandas as pd
# # Load JSON file directly into DataFrame
df = pd.read_json('company_row_data.json')
# Save to CSV
df.to_csv('output_file.csv', index=False)


# # Or
# data = open('company_row_data.json','r')
# df  = pd.read_json(data)
# df.to_csv('output_file.csv', index=False)