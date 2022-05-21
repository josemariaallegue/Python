import pandas as pd
from pathlib import Path
import os

i = 1
for folder, _, files in os.walk(Path(r"D:\Documentos\GitHub\Python\Data Analysis - Wes Mckinney\Chapter-8 (Plotting and Visualization)")):
    for file in files:
        print(file)
        os.rename(Path(folder, file), Path(folder, "9-" + str(i) + ".py"))
        i += 1
