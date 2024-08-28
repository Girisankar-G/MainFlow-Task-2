"""
Pandas Data Analysis:
    * Pandas is a powerful Python library for data manipulation and analysis.
    * It provides data structures like Series and DataFrame to work with structured data.
"""

# Importing Pandas
import pandas as pd

"""
Reading CSV Files:
    * Pandas allows reading CSV files using the `read_csv` function.
    * The data is stored in a DataFrame, which is a 2-dimensional labeled data structure.
"""
# Reading a CSV file into a DataFrame
df = pd.read_csv('Iris.csv')

# Displaying the first few rows of the DataFrame
print(df.head())

"""
Data Cleaning:
    * Handling Missing Values: Pandas provides methods to handle missing data in a DataFrame.
    * Removing Duplicates: Use `drop_duplicates` to remove duplicate rows.
"""
# Handling missing values by filling with a default value or removing
df_filled = df.fillna(0)  # Filling missing values with 0
df_dropped = df.dropna()  # Dropping rows with missing values

# Removing duplicates
df_unique = df.drop_duplicates()

# Displaying the cleaned DataFrame
print(df_unique.head())

"""
Data Manipulation:
    * Filtering: Selecting rows based on a condition.
    * Sorting: Ordering the data based on one or more columns.
    * Grouping: Aggregating data based on a specific column.
"""
# Filtering rows where a specific condition is met
filtered_df = df[df['Id'] > 10]

# Sorting the DataFrame by a specific column
sorted_df = df.sort_values(by='Id')

# Grouping data and performing an aggregate operation
grouped_df = df.groupby('Id').sum()

# Displaying the manipulated DataFrame
print(grouped_df.head())
