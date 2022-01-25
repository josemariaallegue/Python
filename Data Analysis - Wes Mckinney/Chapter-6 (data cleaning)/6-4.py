import pandas as pd

print("Transforming Data Using a Function or Mapping\n")

df = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                            'Pastrami', 'corned beef', 'Bacon',
                            'pastrami', 'honey ham', 'nova lox'],
                   'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}


print(df)
print()

df["food"].str.lower()
print(df)
print()

df["animal"] = df["food"].map(meat_to_animal)
print(df)
# equivalente al punto anterior
df["animal"] = df["food"].map(lambda x: meat_to_animal[x.lower()])
