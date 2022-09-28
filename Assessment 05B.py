# Anh Nguyen
# CSCI 102 - Section B
# Assessment 05A
# References: None
# Time: 40 minutes

total_drank = 0 # Initial variable to track total amount drank
extra = 0 # Will be used to track remainder
result = 0 # Will be used later to help with calculations

# Getting inputs
empty = int(input("EMPTIES> "))
found_empty = int(input("FOUND> "))
cost = int(input("COST> "))
total_empty = empty + found_empty # Combining the amount of empty cans 
index = 0 # Prevents and infinite loop

# Processing the amount Blaster can drink
while total_empty != 0 and index < 999:
  extra = total_empty % cost
  result = total_empty // cost
  total_empty = result + extra
  total_drank += result
  index += 1

print("OUTPUT ", total_drank)
