import os
import re

lastDate = "E:\\Imagenes\\Instagram\\devonjenelle\\2018-02-13_23-12-47_UTC.jpg"
route = "E:\\Imagenes\\Instagram"
instagramProfile = "devonjenelle"
routeFull = os.path.join(route, instagramProfile)
print(re.search(r'(\d+-\d+-\d+)', lastDate).group())

lastDateFinal = lastDate[len(lastDate) - len(routeFull) + 5:len(lastDate) -
                         len(routeFull) + 15]

print(lastDateFinal)