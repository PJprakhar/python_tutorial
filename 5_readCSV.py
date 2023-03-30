import pandas as pd

# 1. Input
raw_data = pd.read_csv("Menu.csv")
print(raw_data)

# 2. Process 
Length =len(raw_data)
sorted = raw_data.sort_values ("Menu", ascending=True)

# 3. Output 
print(f"No of items: {Length}")
print(f'{sorted}')