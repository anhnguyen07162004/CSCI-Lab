# Anh Nguyen
# CSCI 102 - Section B
# Assessment 11
# References: https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/
# Time: 55 minutes

import math

def print_output(anything):
  print(f"OUTPUT {anything}")

def cylinder_vol(radius, height):
  volume = (3.1415 * (radius ** 2)) * height
  print_output(f"{volume:.2f}")

def lbs_to_kg(num):
  num = num * 0.4536
  print_output(f"{num:.4f}")

def polar_coords(x, y):
  r_num = math.sqrt((x ** 2) + (y ** 2))
  theta_num = math.degrees(math.atan(y/x))
  print_output(f"r: {r_num:.2f}")
  print_output(f"theta: {theta_num:.2f}")

def yen_to_dollars(yen):
  yen = yen * 0.0068
  print_output(f"{yen:.2f}")

def quad_form(a, b, c):
  small = 0
  big = 0

  dis = b * b - 4 * a * c
  sqrt_val = math.sqrt(abs(dis))
  sol1 = (-b + sqrt_val)/(2 * a)
  sol2 = (-b - sqrt_val)/(2 * a)

  if sol1 < sol2:
    small = sol1
    big = sol2
  else:
    small = sol2
    big = sol1

  print_output(f"{int(small)}")
  print_output(f"{int(big)}")

polar_coords(12, 5)
