from operator import index
import pandas as pd
import seaborn as sns
from pathlib import Path


df = pd.read_csv(Path(r"Files\cardio_train.zip"), sep=";",
                 encoding="utf8", header=0, index_col=False)

df = pd.DataFrame({"columna1":1, "columna2":2})

print(df)

