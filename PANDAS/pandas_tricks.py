import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 70000, 55000],
    'city': ['NYC', 'LA', 'Chicago', 'NYC']
})

# Trick 1: Multiple conditions with query()
high_earners = df.query('age > 27 and salary > 55000')

# Trick 2: Chain operations
result = (df
    .groupby('city')['salary']
    .mean()
    .round(2)
)

# Trick 3: Memory usage optimization
df['city'] = df['city'].astype('category')

# Trick 4: Quick value counts with normalize
city_pct = df['city'].value_counts(normalize=True)

# Trick 5: Apply with lambda for quick transformations
df['salary_k'] = df['salary'].apply(lambda x: f"{x//1000}k")

# Trick 6: Boolean indexing shortcut
young_workers = df[df.age < 30]

# Trick 7: Quick describe for specific columns
stats = df[['age', 'salary']].describe()

print("DataFrame:")
print(df)
print("\nHigh earners:")
print(high_earners)
print("\nAverage salary by city:")
print(result)
