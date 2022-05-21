import pandas as pd

print("Hierarchical Indexing\n")

# doble indexacion en
df = pd.DataFrame({'num_legs': [4, 4, 2, 2],
                  'num_wings': [0, 0, 2, 2],
                   'class': ['mammal', 'mammal', 'mammal', 'bird'],
                   'animal': ['cat', 'dog', 'bat', 'penguin'],
                   'locomotion': ['walks', 'walks', 'flies', 'walks']})

df = df.set_index(['class', 'animal', 'locomotion'])
print(df)
print()
# seleccion de un elemento en el primer indece
print(df.xs("mammal"))
print()
# seleccion de 2 elementos en indices continuos
print(df.xs(("mammal", "cat")))
print()
# seleccion de 2 elementos en indeces no continuos
print(df.xs(("mammal", "walks"), level=["class", "locomotion"]))
print()
# seleccion de indece que no es el primero
print(df.xs("cat", level=1))
print()
# seleccion de columnas
print(df.xs("num_legs", axis=1))
print()
#print(df.xs("walks", level=2)["num_legs"])
print(df[df["num_wings"] > 1].xs("flies", level=2))
