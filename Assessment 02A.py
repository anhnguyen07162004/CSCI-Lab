# Anh Nguyen
# CSCI 102 - Section B
# Assessment 02A
# Searched up why my float wasn't rounding to 2 decimal places
# Time: 15 minutes

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
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quotient = round((num1 / num2))
remainder = round((num1 % num2))

# Printing outputs
print("OUTPUT ", sum)
print("OUTPUT ", diff)
print("OUTPUT ", prod)
print("OUTPUT ", quotient)
print("OUTPUT ", "%.2f" % remainder)
