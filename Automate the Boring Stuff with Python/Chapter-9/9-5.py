from pathlib import Path
import os

print("Reading and writing files - more about paths")
# modulos para chequear si los paths son absolutos o relativo

print(Path.cwd().is_absolute())
print("")

# devuelve el path absoluto desde uno relativo
print(os.path.abspath("."))
print("")

# devuelve si el path es absoluto (true) o relativo (false)
print(os.path.isabs("."))
print("")
