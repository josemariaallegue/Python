import pandas as pd
from pathlib import Path
import os

data = pd.read_csv(Path(r"Archivos\spx.csv"))
print(data)