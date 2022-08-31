# Anh Nguyen
# CSCI 102 – Section B
# Assessment 01B
# Youtube video about optimization, asking a peer for simple explanation
# Time: 30 minutes


print("Input the total length of fencing available (in yards).")

length_yards = int(input("LENGTH> "))

length_x_yards = (length_yards / 2) / 2
length_y_yards = length_x_yards

length_x_feet = length_x_yards * 3
length_y_feet = length_y_yards * 3

max_area = round(length_x_feet * length_y_feet, 1)

print("The maximum rectangular area that can be bound (in feet) is:")
print("OUTPUT " , max_area)
