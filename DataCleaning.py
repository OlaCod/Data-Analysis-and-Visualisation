import pandas as pd

# Read the CSV file without header
df = pd.read_csv('FILE_NAME.csv', header=None)


# Define the list of URLs to remove
urls_to_remove = [
    'https://WEBSITE',
    'https://WEBSITE'
   
]

# Apply the cleaning process to each row
for index, row in df.iterrows():
    if not pd.isna(row[3]):  # Check if the 'Website' column is not NaN
        cleaned_urls = [url for url in row[3].split(', ') if url not in urls_to_remove]
        df.at[index, 3] = ', '.join(cleaned_urls)

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False, header=False)
