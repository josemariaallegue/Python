import json

print("JSON")

# JSON a python
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
print(json.loads(stringOfJsonData))

# python a JSON
pythonValue = {'isCat': True, 'miceCaught': 0,
               'name': 'Zophie', 'felineIQ': None}
print(json.dumps(pythonValue))
