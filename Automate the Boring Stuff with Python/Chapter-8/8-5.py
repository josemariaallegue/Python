import pyinputplus as pyip

# validaciones custom
print("Input validation - Custom Validation Function to inputCustom()")

# se crea una funcion y luego es pasado a inputCustom()


def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
                        (sum(numbersList)))

    return int(numbers)  # Return an int form of numbers.


response = pyip.inputCustom(addsUpToTen)  # No parentheses after
