import pyinputplus as pyip
import random

cantidadSanwich = 0
precio = 0
ingredients = []

ingredients.append(pyip.inputMenu(
    ["wheat", "white", "sourdough"], "What kind of bread do you want?\n"))
print("")

ingredients.append(pyip.inputMenu(
    ["chicken", "turkey", "ham", "tofu"], "What kind of protein do you want?\n"))
print("")

print("Cheese? ")
if("yes" == str(pyip.inputYesNo()).lower()):
    ingredients.append(pyip.inputMenu(
        ["cheddar", "swiss", "mozzarella"], "What kind?\n"))
    print("")

for dressing in ["mayo", "mustrard", "lettuce", "tomato"]:

    ingredients.append(pyip.inputYesNo(f"Do you want {dressing}? "))
print("")

cantidadSanwich = pyip.inputInt("How many sandwiches? ", min=1)
print("")

for ingredient in ingredients:
    precio += random.uniform(1, 5)

print(f"The final price of your order is {round(precio,2) * cantidadSanwich}")
