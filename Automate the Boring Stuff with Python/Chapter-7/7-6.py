import re
# se puden crear clases propias con []
print(r"Expresiones regulares - character classes []")

# en este casos trae todos las vocales del string
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print("")

# en este casos trae todos las consonantes porque se agrego el ^
print("Expresiones regulares - ^")
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print("")

# en este casos trae todos las mayusculas del string
# - estable el rango para evitar copiar todas las posibilidades
print("Expresiones regulares - '.'")
vowelRegex = re.compile(r'[A-Z]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
