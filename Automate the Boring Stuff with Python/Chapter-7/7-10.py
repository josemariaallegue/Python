import re
print(r"Expresiones regulares - sub()")

# substituye un patron encontrado con otro texto
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
print("")

# el "\1****" permite dejar solo el caracter encontrado en el primer grupo, en este caso la primer letra del nombre
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****',
      'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
