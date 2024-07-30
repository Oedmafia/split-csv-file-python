import pandas as pd

def split_csv_into_chunks(csv_file_name, lines_per_file):
    # Read the CSV file in chunks
    for i, chunk in enumerate(pd.read_csv(csv_file_name, chunksize=lines_per_file)):
        # Create the name for the new CSV file
        new_file_name = f"{csv_file_name.replace('.csv', '')}_part_{i + 1}.csv"
        
        # Save the chunk to a new CSV file
        chunk.to_csv(new_file_name, index=False)
        print(f"Saved file: {new_file_name}")

# Use the function
csv_file_name = 'base.csv'  # Replace with the name of your CSV file or change the name of your file to "base.csv"
lines_per_file = 49999  # Number of lines per file
split_csv_into_chunks(csv_file_name, lines_per_file)
