import pandas as pd
import numpy as np

print("Permutation and Random Sampling\n")

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
print(df)
print()

# Calling permutation with the length of the axis you want
# to permute produces an array of integers indicating the new ordering
sampler = np.random.permutation(5)
print(sampler)
print()

# reorganiza el df a travez del sampler
print(df.iloc[sampler])
# print(df.take(sampler))  # equivalente al punto anterior
print()

# devuelve una reorganizacion del df sin modificar el elemento original
# si se pone replace=True se modificar el elemento original
print(df.sample(n=3, replace=False))
