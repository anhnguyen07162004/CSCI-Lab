# Anh Nguyen
# CSCI 102 - Section B
# Assessment 06A
# References: None
# Time: 10 minutes

num = int(input("NUMBER> "))
index = int(input("INDEX> "))
output_table = []

for i in range (1, index + 2):
  output_table.append(num * i)

print("OUTPUT", output_table)
print("OUTPUT", num)
