import pandas as pd

print("Combining Data with Overlap\n")

df1 = pd.DataFrame({'A': [None, 0],
                    'B': [None, 4]})
df2 = pd.DataFrame({'A': [1, 1],
                    'B': [3, None]})
print(df1)
print()
print(df2)
print()

# Combine two DataFrame objects by filling null values in
# one DataFrame with non-null values from other DataFrame
print(df1.combine_first(df2))
print()

# Null values still persist if the location of that null value does not exist in other
df3 = pd.DataFrame({'A': [None, 0], 'B': [4, None]})
df4 = pd.DataFrame({'B': [3, 3], 'C': [1, 1]}, index=[1, 2])
print(df3.combine_first(df4))
