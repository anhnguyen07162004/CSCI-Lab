# Anh Nguyen
# CSCI 101 – Section G
# Python Assessment 1
# References: None
# Time: 60+ minutes

# Imports
import math

# Inputs
early = int(input("EARLY> "))
hours_input = int(input("HOURS> "))
mins_input = int(input("MINUTES> "))

# Creating hours and minutes from division and modulo, respectively
hours = math.floor(early / 60)
mins = early % 60

# Outputs
if hours_input - hours <= 0:
  hours2 = 24
  if early > mins_input:
    hours2 = hours2 - 1
    early = early - mins_input
    if early > 60:
      early = early - 60
      mins = 60 - early
      print("OUTPUT", hours2, mins)
    else:
      mins = 60 - early
      print("OUTPUT", hours2, mins)
else:
  hours2 = hours_input
  if early > mins_input:
    hours2 = hours2 - 1
    early = early - mins_input
    if early > 60:
      early = early - 60
      mins = 60 - early
      print("OUTPUT", hours2, mins)
    else:
      mins = 60 - early
      print("OUTPUT", hours2, mins)
