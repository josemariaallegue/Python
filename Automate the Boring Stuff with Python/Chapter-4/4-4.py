print("Los string son similares a las listas")
name = 'Zophie'
name[0]
name[-2]
name[0:4]
'Zo' in name
'z' in name
'p' not in name
for i in name:
    print('* * * ' + i + ' * * *')
print("")

print("pero no son muteables")
try:
    name = 'Zophie a cat'
    name[7] = 'the'
except:
    print("error")

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name
print(newName)