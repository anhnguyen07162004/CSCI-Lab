# Anh Nguyen
# CSCI 102 - Section B
# Assessment 05A
# References: None
# Time: 25 minutes

# Initial variable to track total amount drank
total_drank = 0
total_full = 0
result = 0 # Will be used later to help with calculations

# Getting inputs
empty = int(input("EMPTIES> "))
found_empty = int(input("FOUND> "))
cost = int(input("COST> "))
total_empty = empty + found_empty # Combining the amount of empty cans 

# Processing the amount Blaster can drink
while total_empty != 0:
  if total_empty < cost:
    break
  else:
    result = total_empty // cost
    total_empty = total_empty - result
    total_drank += result

print("OUTPUT ", total_drank)
