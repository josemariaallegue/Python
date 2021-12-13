
print("Functions are objects\n")

# al tener en cuenta es se puede psar una funcion como parametro de otra funcion

states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south carolina##', 'West virginia?']


clean_ops = [str.strip, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result


print(clean_strings(states, clean_ops))
