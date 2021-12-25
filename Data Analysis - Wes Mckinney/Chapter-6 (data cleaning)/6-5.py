import pandas as pd

print("Replacing Values\n")

serie = pd.Series([1., -999., 2., -999., -1000., 3.])

print(serie)
print()
print(serie.replace([-999, 2], ["null", "null2"]))
print()
# equivalente al punto anterior
print(serie.replace({-999: "null", 2: "null2"}))
