import pandas as pd
import numpy as np

# Input file name
filename = 'priceTest.csv'

# Read the input file into a pandas DataFrame
df = pd.read_csv(filename)

# Generate a sequence of unique numbers using numpy
unique_numbers = np.arange(1, len(df) + 1)

# Assign the sequence of unique numbers to a new column in the DataFrame
df['ID_Number'] = unique_numbers

#Rename IP Expected Reimbursement and OP Expected Reimbursement to just IP and OP. 
# This will be appended into each Plans. This will resulce header length instead of the whole IP Expected Reimbursement or OP Expected Reimbursement
df_Rename = df.rename(columns={'IP Expected Reimbursement': 'IP', 'OP Expected Reimbursement': 'OP'})

# Replace spaces in column names with underscores
df_Rename.columns = [col.replace(' ', '_') for col in df_Rename.columns]

# Select the columns to include in the output
df_Rename = df_Rename[['ID_Number', 'Code_type', 'Code', 'Procedure_Description', 'NDC', 'Rev_Code', 'IP_Price', 'OP_Price', 'Plan(s)', 'IP', 'OP']]
print(df_Rename.shape)


# Pivot the DataFrame on the 'Plan(s)' column
df_Rename = df_Rename.pivot(index=['ID_Number','Code_type', 'Code', 'Procedure_Description', 'NDC', 'Rev_Code', 'IP_Price', 'OP_Price'], columns='Plan(s)', values=['IP', 'OP'])
print(df_Rename)

# This is pending -------------------------
# Handle duplicates in the 'Plan(s)' column by aggregating with the mean
#df_Rename = df_Rename.groupby(['ID_Number', 'Code_type', 'Code', 'Procedure_Description', 'NDC', 'Rev_Code', 'IP_Price', 'OP_Price']).mean().reset_index()
#print(df_Rename)
#------------------------------------------------

# Flatten the column names in the pivot table
df_Rename.columns = df_Rename.columns.map('_'.join)


df_Rename.columns = df_Rename.columns.map(lambda x: x.split('_')[::-1]).map('_'.join)

# Reset the index to include the original columns in the output
df_Rename = df_Rename.reset_index()


# Get the subset of columns to sort
cols_to_sort = [col for col in df_Rename.columns if '_IP' in col or '_OP' in col]

# Sort the subset of columns alphabetically
df_Rename = df_Rename.reindex(columns=sorted(cols_to_sort) + [col for col in df_Rename.columns if col not in cols_to_sort])

# Get the columns to keep in front
cols_to_keep_in_front = ['Code_type', 'Code', 'Procedure_Description', 'NDC', 'Rev_Code', 'IP_Price', 'OP_Price']


# Sort the subset of columns alphabetically
df_Rename = df_Rename[cols_to_keep_in_front + sorted(cols_to_sort)]

# Get the minimum and maximum values for the columns with '_IP'
cols_ip = [col for col in df_Rename.columns if '_IP' in col]
min_ip = df_Rename[cols_ip].min(axis=1)
max_ip = df_Rename[cols_ip].max(axis=1)

# Get the minimum and maximum values for the columns with '_OP'
cols_op = [col for col in df_Rename.columns if '_OP' in col]
min_op = df_Rename[cols_op].min(axis=1)
max_op = df_Rename[cols_op].max(axis=1)


# Add the minimum and maximum values as new columns
df_Rename['MIN_IP'] = min_ip
df_Rename['MAX_IP'] = max_ip
df_Rename['MIN_OP'] = min_op
df_Rename['MAX_OP'] = max_op

# Output file name
output_filename = 'output2.csv'

# Write the output to a CSV file
df_Rename.to_csv(output_filename, index=False)


