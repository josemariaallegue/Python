import pandas as pd
import numpy as np

print("Operations between DataFrame and Series\n")

df = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                  columns=list("bde"),
                  index=["utah", "ohio", "texas", "oregon"])

serie = df.iloc[0]

print(serie)
print()
print(df)
print()

"""By default, arithmetic between DataFrame and Series matches the index of the Series
on the DataFrame’s columns, broadcasting down the rows"""
print(df+serie)
print()


"""If an index value is not found in either the DataFrame’s columns or the Series’s index,
the objects will be reindexed to form the union"""
serie2 = pd.Series(range(3), index=["b", "e", "f"])

print(df + serie2)
print()

"""If you want to instead broadcast over the columns, matching on the rows, you have to
use one of the arithmetic methods."""
serie3 = df["d"]
print(df.sub(serie3, axis="index"))
