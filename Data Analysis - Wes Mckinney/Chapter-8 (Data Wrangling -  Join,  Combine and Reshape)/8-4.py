from functools import reduce
import numpy as np
import pandas as pd


print("Database-Style DataFrame Joins\n")

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})

print(df1)
print()
print(df2)
print()

# inner join
print(pd.merge(df1, df2, on="key"))
print()

# si el nombre de las columnas con el dato a buscar fuera
# distinto se hace
# print(pd.merge(df1, df2, left_on="key", right_on="key"))
# print()

# se puede establecer el tipo de join
# las opciones son: left, right, inner y outer (combinacion de righ con left)
print(df1.merge(df2, how="outer", on="key"))
print()

df3 = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                    'key2': ['one', 'two', 'one'],
                    'val': [1, 2, 3]})

df4 = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                    'key2': ['one', 'one', 'one', 'two'],
                    'val': [4, 5, 6, 7]})

# merge con varios keys
print(df3.merge(df4, how="inner", on=["key1", "key2"]))
print()

# si en ambos df hay columnas con nombres identicos se agregan
# los suffixes "_x" y "_y", estos se puden modificar
print(df3.merge(df4, how="inner", on=[
      "key1", "key2"], suffixes=("_left", "_rigth")))
print()

# merge con por el index
df5 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                    'value': range(6)})
df6 = pd.DataFrame({'group_val': [3.5, 7]},
                   index=['a', 'b'])

print(df5.merge(df6, how="outer", left_on="key", right_index=True))
print()

# merge en df jerarquicamente indexados

df7 = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                             'Nevada', 'Nevada'],
                    'key2': [2000, 2001, 2002, 2001, 2002],
                    'data': np.arange(5.)})
df8 = pd.DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                          'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])

print(df7)
print()
print(df8)
print()
print(df7.merge(df8, how="outer", left_on=["key1", "key2"], right_index=True))
print()

# hacer un merge con cantidad x de df
"""dfs = [df0, df1, df2, dfn]

dfFinal = reduce(lambda dfLeft, dfRight: pd.merge(
    dfLeft, dfRight, how="inner", on="key"), dfs)"""
