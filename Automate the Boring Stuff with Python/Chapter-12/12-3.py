import bs4
import requests

print("Web scraping - BeautifulSoup")
# obtencion de html desde pagina
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

# desde archivo
exampleFile = open(
    r'D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-12\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))
print("")

print("Web scraping - Finding an Element with the select() Method")

exampleFile = open(
    r'D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-12\example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))  # elems is a list of Tag objects.
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))  # The Tag object as a string.
print(elems[0].getText())
print(elems[0].attrs)
print("")

# para obtener los atributos de un elemento
print("Web scraping -get() Method")
spanElem = exampleSoup.select('span')[0]  # solo el primer span
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)
