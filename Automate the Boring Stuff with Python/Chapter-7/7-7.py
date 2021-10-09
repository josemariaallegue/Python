import re
print(r"Expresiones regulares - ^ and $")

# ^ fuera de [] y al principio del regex significa que el texto debe comenzar con el patron
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world!'))
print(beginsWithHello.search('He said hello.'))
print("")

# $ al final del regex significa que el texto debe terminar con el patron
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.'))
print("")

# al combinar ^ y $ se estable que texto debe coincidir en su totalidad con al patron
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890'))
print(wholeStringIsNum.search('12  34567890'))
