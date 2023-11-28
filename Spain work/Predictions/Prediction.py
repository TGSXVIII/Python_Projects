import pandas as pd
import os

# Specify the absolute path to the CSV file
csv_file_path = r'C:\Users\mads020n\Desktop\predicciones.csv'

# Print the current working directory
print("Current working directory:", os.getcwd())

# Check if the file exists
if os.path.exists(csv_file_path):
    print(f"File exists at the specified path: {csv_file_path}")

    # Continue with the rest of your code
    df = pd.read_csv(csv_file_path)

    # List of column names you want to keep
    columns_to_keep = ['TodThickFlow', 'predicciones']

    # Filter the DataFrame to keep only the desired columns
    df_filtered = df[columns_to_keep]

    # Add a new column called 'median' containing the result of subtracting 'TodThickFlow' from 'predicciones'
    df_filtered['median'] = df_filtered['predicciones'] - df_filtered['TodThickFlow']

    # Convert the filtered DataFrame to JSON and save it to a file
    output_json_file_path = 'output_file.json'  # replace with the desired output file path
    df_filtered.to_json(output_json_file_path, orient='records')

    print(f"The filtered data has been saved to {output_json_file_path}")

else:
    print(f"File not found at the specified path: {csv_file_path}")


# List of column names you want to keep
columns_to_keep = ['TodThickFlow', 'predicciones']

# Filter the DataFrame to keep only the desired columns
df_filtered = df[columns_to_keep]

# Add a new column called 'median' containing the result of subtracting 'TodThickFlow' from 'predicciones'
df_filtered['median'] = df_filtered['predicciones'] - df_filtered['TodThickFlow']

# Convert the filtered DataFrame to JSON and save it to a file
output_json_file_path = 'output_file.json'  # replace with the desired output file path
df_filtered.to_json(output_json_file_path, orient='records')

print(f"The filtered data has been saved to {output_json_file_path}")
