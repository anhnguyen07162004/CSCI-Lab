# Anh Nguyen
# CSCI 102 – Section B
# Assessment 03B
# References: Searched up how to include ending 0's after round
# Time: 20 minutes

# Input
num1 = float(input("FIRST> "))
num2 = float(input("SECOND> "))
op = int(input("OPERATION> "))

# Creating outputs (addition, subtraction, multiplication and division respectively)
if op == 1:
  sum = "%.6f" % round(num1 + num2, 6)
  print("OUTPUT ", sum)
elif op == 2:
  diff = "%.6f" % round(num1 - num2, 6)
  print("OUTPUT ", diff)
elif op == 3:
  prod = "%.6f" % round(num1 * num2, 6)
  print("OUTPUT ", prod)
else:
  quotient = round(num1 / num2)
  rem = round(num1 % num2)
  print("OUTPUT ", quotient)
  print("OUTPUT ", rem)
