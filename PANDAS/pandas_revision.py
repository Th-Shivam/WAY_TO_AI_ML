import pandas as pd
import numpy as np

# DataFrame Creation
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df_from_dict = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})

# Reading Data
# df = pd.read_csv('file.csv')
# df = pd.read_excel('file.xlsx')

# Basic Info
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

# Selection
print(df['A'])  # Column
print(df[['A', 'B']])  # Multiple columns
print(df.iloc[0])  # Row by index
print(df.loc[0, 'A'])  # Specific cell

# Filtering
filtered = df[df['A'] > 1]
filtered = df[(df['A'] > 1) & (df['B'] < 6)]

# Adding/Dropping
df['C'] = df['A'] + df['B']
df = df.drop('C', axis=1)
df = df.drop(0, axis=0)

# Groupby
grouped = df.groupby('A').sum()
grouped = df.groupby('A').agg({'B': ['mean', 'sum']})

# Sorting
df_sorted = df.sort_values('A')
df_sorted = df.sort_values(['A', 'B'], ascending=[True, False])

# Missing Data
df.isnull().sum()
df.dropna()
df.fillna(0)

# Merging
df1 = pd.DataFrame({'key': ['A', 'B'], 'val1': [1, 2]})
df2 = pd.DataFrame({'key': ['A', 'B'], 'val2': [3, 4]})
merged = pd.merge(df1, df2, on='key')

# String Operations
df['name'].str.upper()
df['name'].str.contains('A')

# Apply Functions
df['A'].apply(lambda x: x * 2)
df.apply(lambda row: row['A'] + row['B'], axis=1)

# Pivot Tables
pivot = df.pivot_table(values='B', index='A', aggfunc='mean')
