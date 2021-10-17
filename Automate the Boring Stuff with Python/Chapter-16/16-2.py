import csv
from pathlib import Path

print("CSV files - writing")
path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-16", "example2.csv")

# apertura y creacion del writer
csvFile = open(path, "w", newline="")
csvWriter = csv.writer(csvFile)

csvWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# el objeto detecta la "," del primer elemento y no genera error
csvWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

# segundo ejemplo
path = Path(r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-16", "example3.tsv")
csvFile = open(path, "w", newline="")

# se puede modificar el delimitaror entre elementos de una fila
# se puede modificar el ultimo elemento que viene al final de la fila
# en este caso debemos utilizar ".tsv" en vez de ".csv" porque el delimitador son tabs
csvWriter = csv.writer(csvFile, delimiter="\t", lineterminator="\n\n")

csvWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
csvWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
