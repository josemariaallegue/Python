import re
print(r"Expresiones regulares - the wildcard '.'")

# el "." es un comidin pero para un solo caracter
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
print("")

# el "*" es un comidin que trae todos los caracteres luego o antes de algo
print(r"Expresiones regulares - the wildcard '*'")
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
print(mo.group())
print("")


nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
print("")


# el tecnica para agarrar TODOS los caracteres
print(r"Expresiones regulares - Matching Newlines")
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search(
    'Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search(
    'Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
