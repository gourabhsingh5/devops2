import pandas as pd

input_file= 'customer_10k_good_data.csv'
df= pd.read_csv(input_file)
l= len(df)
print(l)
print(df.head())