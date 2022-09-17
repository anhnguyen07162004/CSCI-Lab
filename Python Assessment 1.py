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
      if hours2 < 10:
        print("OUTPUT", "0" + str(hours2), mins)
      else:
        print("OUTPUT", hours2, mins)
    else:
      mins = 60 - early
      if hours2 < 10:
        print("OUTPUT", "0" + str(hours2), mins)
      else:
        print("OUTPUT", hours2, mins)
  elif early == mins_input:
    mins = "00"
    if hours2 < 10:
      print("OUTPUT", "0" + str(hours2), mins)
    else:
      print("OUTPUT", hours2, mins)
  else:
    mins = mins_input - early
    if hours2 < 10:
      print("OUTPUT", "0" + str(hours2), "0" + str(mins))
    else:
      print("OUTPUT", hours2, "0" + str(mins))
else:
  hours3 = hours_input
  if early > mins_input:
    hours3 = hours3 - 1
    early = early - mins_input
    if early > 60:
      early = early - 60
      mins = 60 - early
      if hours3 < 10:
        print("OUTPUT", "0" + str(hours3), mins)
      else:
        print("OUTPUT", hours3, mins)
    else:
      mins = 60 - early
      if hours3 < 10:
        print("OUTPUT", "0" + str(hours3), mins)
      else:
        print("OUTPUT", hours3, mins)
  elif early == mins_input:
    mins = "00"
    if hours3 < 10:
      print("OUTPUT", "0" + str(hours3), mins)
    else:
      print("OUTPUT", hours3, mins)
  else:
    mins = mins_input - early
    if hours3 < 10:
      print("OUTPUT", "0" + str(hours3), "0" + str(mins))
    else:
      print("OUTPUT", hours3, "0" + str(mins))
