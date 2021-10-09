print("setDefault()")

spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault("color", "black"))
print(spam)
print(spam.setdefault("color", "whiete"))  # no lo cambia a blanco porque ya esta seteado negro como default
