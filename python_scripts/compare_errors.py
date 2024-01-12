import pandas as pd

# Create a DataFrame for known errors with the shared column names
known_errors_df = pd.DataFrame(columns=['error_type', 'error_description'])

# Populate known_errors_df with error data (sample data)
known_errors_data = [
    {'error_type': 'Missing Data', 'error_description': 'Missing customer_id detected'},
    {'error_type': 'Missing Data', 'error_description': 'Missing order_timestamp detected'},
    {'error_type': 'Data Type Mismatch', 'error_description': 'Data type mismatches detected'},
    # Add more error data as needed
]

# Append error data to known_errors_df
known_errors_df = known_errors_df.append(known_errors_data, ignore_index=True)

# Extract and save the column names to shared_column_names.csv
shared_column_names = known_errors_df.columns.tolist()
shared_column_names_df = pd.DataFrame({'column_name': shared_column_names})
shared_column_names_df.to_csv('shared_column_names.csv', index=False)

# Save known_errors_df to CSV
known_errors_df.to_csv('known_errors.csv', index=False)

# Noisy Customers DataFrame
    # Add alternate name spellings (10% chance)
    # Introduce partial and invalid email addresses (10% chance)
    # Introduce partial and invalid phone numbers (10% chance)
# Noisy Products DataFrame
    # Add alternate name spellings (10% chance)
    # Introduce outlier prices (5% chance)
# Noisy Orders DataFrame
    # Introduce random null values (10% chance)
    # Corrupt some percentage of order dates (10% chance)
    # Introduce alternate character encodings (5% chance)
    # Introduce missing or invalid delimiters (5% chance)
    # Introduce outlier #units (5% chance)
    # Introduce outlier prices (5% chance)
    # Create some percentage of data integrity errors (5% chance)

"""
 Missing Data : Missing customer_id detected
 Missing Data : Missing order_timestamp detected
 Duplicate Records : Duplicate records detected
 Data Type Mismatch : Data type mismatches detected
 Invalid Date Format : Invalid date formats detected
 Invalid Date : Invalid dates detected
 Outlier Quantity : Outlier quantities detected
 Outlier Price : Outlier prices detected
 Data Integrity Errors : Data integrity errors detected
 String Encoding Errors : String encoding errors detected
 
 Data Wrangling Tools 2023
 Parsehub
 Scrapy
 Talend
 Alteryx APA Platform
 Altair Monarch
 Microsoft Power Query
 Tableau Desktop
 Trifacta
 Datameer
 R Studio
 OpenRefine
 Tidyverse
 The babynames package
 
 
 
 
 
"""
 