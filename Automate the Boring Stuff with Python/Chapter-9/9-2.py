from pathlib import Path
import os

print("Reading and writing files - directory")
""" Every program that runs on your computer has a current working directory, or cwd. Any filenames 
or paths that do not begin with the root folder are assumed to be under the current working directory."""

# current working directory
print(Path.cwd())
# cambiando cwd
os.chdir(r"C:\Windows\System32")
print(Path.cwd())
print("")

# home directory
print(Path.home())
