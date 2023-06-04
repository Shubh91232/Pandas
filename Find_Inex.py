# Pandas
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 8, 10],
        'C': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

# Find index numbers for a specific element value
element_value = 8
index_numbers = df.index[df['B'] == element_value].tolist()

print(index_numbers)
