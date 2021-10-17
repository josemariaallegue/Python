import csv
from pathlib import Path

print("CSV files - reading")
path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-16", "example.csv")

# apertura y creacion del reader
csvFile = open(path, "r")
csvReader = csv.reader(csvFile)

# solo es posible una lectura por apertura salvo que se corra el "puntero"
# distintas formas de lectura
# print(list(csvReader))

# for line in list(csvReader):
#    print(str(line))

for line in csvReader:
    print('Line #' + str(csvReader.line_num) + ' ' + str(line))
