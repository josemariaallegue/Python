import pyinputplus as pyip

# regex para validar aun mas el ingreso de valores
print("Input validation - The allowRegexes and blockRegexes Keyword")

# allowRegexes permite valores que anteriormente no serian validos
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])

# blockRegexes bloquea valores que anteriormente no serian validos
response = pyip.inputNum(blockRegexes=[r'[02468]$'])

# si se pasan allow y block en el mismo input allow sobreescribe al block
response = pyip.inputStr(
    allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
