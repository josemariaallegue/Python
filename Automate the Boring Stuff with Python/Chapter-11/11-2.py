
print("Debugging - try, exception and raise exception")
"""An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. 
These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError 
exception is raised. In code, an assert statement consists of the following:

The assert keyword
A condition (that is, an expression that evaluates to True or False)
A comma
A string to display when the condition is False
In plain English, an assert statement says, 
“I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.”"""

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1]   # Assert that the first age is <= the last age

ages.sort(reverse=True)
assert ages[0] <= ages[-1]  # genera error
