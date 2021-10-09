import requests
import bs4
from pathlib import Path
import logging

pathBase = "https://xkcd.com/"
pathGuardado = Path(
    r"D:\Documentos\GitHub\Python\Automate the Boring Stuff with Python\Archivos auxiliares\Chapter-12\xkcd")

while not pathBase.endswith('#'):

    requestPage = requests.get(pathBase)
    requestPage.raise_for_status()
    soupObject = bs4.BeautifulSoup(requestPage.text, "html.parser")

    elements = soupObject.select("div #comic > img")

    for element in elements:

        requestFile = requests.get(pathBase + element.get("src"))
        requestFile.raise_for_status()

        with open(Path(pathGuardado, element.get("src").split("/")[-1]), "wb") as file:

            for chunk in requestFile.iter_content(100000):
                file.write(chunk)
            logging.debug(f"Archivo {file.name} guardado")

    # Get the Prev button's url.
    prevLink = soupObject.select('a[rel="prev"]')[0]
    pathBase = 'https://xkcd.com' + prevLink.get('href')
