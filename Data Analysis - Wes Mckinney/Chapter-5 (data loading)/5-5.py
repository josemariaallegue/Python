import pandas as pd
import requests
from pathlib import Path

print("Interacting with Web APIs\n")

ruta = Path(
    r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Archivos\example4.json")
url = "https://api.github.com/repos/pandas-dev/pandas/issues"

resp = requests.get(url)
data = resp.json()
df = pd.DataFrame(data, columns=["number", "title", "labels", "state"])
print(df)
