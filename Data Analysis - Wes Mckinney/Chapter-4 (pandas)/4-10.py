import pandas as pd
import numpy as np

print("Function Application and Mapping\n")

"""NumPy ufuncs (element-wise array methods) also work with pandas objects"""

df = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df)
print()
print(np.abs(df))
print()

"""Another frequent operation is applying a function on one-dimensional arrays to each
column or row. DataFrame’s apply method does exactly this."""


def f(x): return x.max() - x.min()


print(df.apply(f))
print()

"""Element-wise Python functions can be used, too. Suppose you wanted to compute a
formatted string from each floating-point value in frame. You can do this with apply
map"""


def format(x): return "%.2f" % x


print(df.applymap(format))
