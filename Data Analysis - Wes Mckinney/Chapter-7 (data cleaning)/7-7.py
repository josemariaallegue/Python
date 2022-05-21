import pandas as pd
import numpy as np

print("Discretization and Binning\n")

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
print()
print(cats.codes)
print()
print(cats.categories)
print()
# Consistent with mathematical notation for intervals, a parenthesis means that the side
# is open, while the square bracket means it is closed (inclusive)
# You can change which side is closed by passing right = False
print(pd.value_counts(cats))
print()
cats2 = pd.cut(ages, bins, labels=[
    'Youth', 'Young adult', 'Middle aged', 'Senior'],
    right=False)
print()
print(pd.value_counts(cats2))
print()
