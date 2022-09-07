# Anh Nguyen
# CSCI 102 - Section B
# Assessment 02A
# Searched up why my float wasn't rounding to 2 decimal places
# Time: 15 minutes

import math
# Variables for operators
sum = 0.0
diff = 0.0
quotient = 0.0
prod = 0.0
remainder = 0.0

# Saving inputs
print("Input the first operand.")
num1 = float(input("FIRST> "))
print("Input the second operand.")
num2 = float(input("SECOND> "))

# Creating outputs
sum = round((num1 + num2), 1)
diff = round((num1 - num2), 1)
prod = round((num1 * num2), 1)
quotient = math.floor(num1 / num2)
remainder = (num1 % num2)

# Printing outputs
print("OUTPUT ", sum)
print("OUTPUT ", diff)
print("OUTPUT ", prod)
print("OUTPUT ", quotient)
print("OUTPUT ", "%.2f" % remainder)
