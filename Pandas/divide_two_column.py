import pandas as pd

# take inputs
df = pd.DataFrame({'column1':[4,9,10,15], 'column2':[2,3,5,15]})
# divide columns
df['division'] = df['column1'] / df['column2']

# print division value
print(df)