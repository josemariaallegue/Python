import csv
from pathlib import Path

path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-16\Practica-1")
flag = False

for file in path.glob("*.csv"):
    with open(file, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        csvList = list(csvReader)
        del csvList[0]

    with open(file, "w", newline="") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(csvList)
        """for item in csvList:
            csvWriter.writerow(item)"""
