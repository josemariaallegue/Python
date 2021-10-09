import pyinputplus as pyip
import requests
import bs4
import webbrowser

busqueda = pyip.inputStr("Ingrese el termino a buscar: ")
pathBase = "https://pypi.org/"
pathSearch = "https://pypi.org/search/?q="

request = requests.get(pathSearch + busqueda)
request.raise_for_status()

soupObject = bs4.BeautifulSoup(request.text, "html.parser")
elements = soupObject.select(".package-snippet")

cantidadMinima = min(5, len(elements))

print("Searching...")
for i in range(cantidadMinima):
    webbrowser.open(pathBase + elements[i].get("href"))
