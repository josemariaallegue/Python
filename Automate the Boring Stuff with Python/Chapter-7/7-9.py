import re
print(r"Expresiones regulares - ignorcase()")

# evita que se tenga en cuentra las mayusculas y minusculas en la busqueda
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search(
    'Al, why does your programming book talk about robocop so much?').group())
