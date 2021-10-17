import csv
from pathlib import Path

print("CSV files - reading/writing dicctionary")
path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-16", "exampleHeader.csv")

csvFile = open(path, "r")
# conviene usar DictReader cuando el .csv contiene un header
csvReader = csv.DictReader(csvFile)

for row in csvReader:
    print(row['id'], row['first_name'], row['email'])


path2 = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-16", "output.csv")
# apertura y creacion del writer
csvFile = open(path2, "w", newline="")
csvWriter = csv.DictWriter(csvFile, ['Name', 'Pet', 'Phone'])
csvWriter.writeheader()  # hay que ponerlo para que aparesca el header
csvWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
csvWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
