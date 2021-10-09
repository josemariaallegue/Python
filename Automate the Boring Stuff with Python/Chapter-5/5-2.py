print("Revisar el contenido de un diccionario")
spam = {'name': 'Zophie', 'age': 7}

print("name" in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print("")

print("get() method")
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') # devuelve el segundo parametro si el primero no esta
print('I am bringing 2 cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
print('I am bringing 0 eggs.')

