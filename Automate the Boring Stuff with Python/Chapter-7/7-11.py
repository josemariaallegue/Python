import re
print(r"Expresiones regulares - re.verbose()")

# permite dividir el patron en varias lineas para facilitar la lectura
# se tiene que agregar el triple "
phoneRegex = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
print("")

# por si se quiere pasar mas de un parametro a re.compile se pone |
omeRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
