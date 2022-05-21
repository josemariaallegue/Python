import numpy as np
import pandas as pd

print("Reshaping with Hierarchical Indexing\n")

df = pd.DataFrame(np.arange(6).reshape((2, 3)),
                  index=pd.Index(['Ohio', 'Colorado'], name='state'),
                  columns=pd.Index(['one', 'two', 'three'], name='number'))

print(df)
print()

# Return a reshaped DataFrame or Series having a multi-level index
# with one or more new inner-most levels compared to the current
# DataFrame. The new inner-most levels are created by pivoting the
# columns of the current dataframe:
print(df.stack())
print()

# Returns a DataFrame having a new level of column labels whose
# inner-most level consists of the pivoted index labels.
print(df.stack().unstack())
print()
# se puede definir que nivel es desapilado
# tambien se pueden utilizar numeros
# tambien se puede definir que nivel es apilado
print(df.stack().unstack("state"))
print()

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
df2 = pd.concat([s1, s2], keys=['one', 'two'])

# unstack proudce NaN si faltan elementos
print(df2.unstack())
print()
# pero a la inversa los quita salvo que se ponga dropna=False
print(df2.unstack().stack(dropna=False))
