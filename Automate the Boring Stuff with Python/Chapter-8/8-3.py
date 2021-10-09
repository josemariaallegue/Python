import pyinputplus as pyip

print("Input validation - limit, timeout, and default Keyword ")
response = pyip.inputNum(limit=2)
response = pyip.inputNum(timeout=1)
print("")

# default para evitar la elevacion del error
response = pyip.inputNum(limit=2, default='N/A')
