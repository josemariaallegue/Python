import os
from pathlib import Path
import shutil

path = Path(r"E:\Games\Roms\Temp")

for folder, _, files in os.walk(path):
    for file in files:
        shutil.move(Path(folder, file), Path(path, file))
print("Finish")
