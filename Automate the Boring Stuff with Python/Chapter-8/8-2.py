import pyinputplus as pyip

print("Input validation - min, max, greaterThan, and lessThan Keyword ")

response = pyip.inputNum('Enter num: ', min=4)
response = pyip.inputNum('Enter num: ', greaterThan=4)
response = pyip.inputNum('>', min=4, lessThan=6)
print("")

# no se puede dejar el input vacio salvo que se lo determine
response = pyip.inputNum('Enter num: ')
response = pyip.inputNum(blank=True)
