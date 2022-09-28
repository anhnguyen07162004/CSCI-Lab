# Anh Nguyen
# CSCI 102 - Section B
# Assessment 05A
# References: None
# Time: 10 minutes

# Creating variables
input_list = []
index1 = 0
index2 = 0
user_input = ""
big_num = 100**100 # Big number so that the program continues to run until quit is entered
num_num = 0 # Tracks the number of numbers inputted
sum = 0 # Tracks the sum of the numbers inputted

while index1 < big_num:
  user_input = input("NUMBER> ")
  if user_input == "quit":
    break
  else:
    input_list.append(int(user_input))
    index1 += 1

while index2 < len(input_list):
  num_num += 1
  sum += input_list[index2]
  index2 += 1

print("OUTPUT", num_num, "numbers")
print("OUTPUT", sum, "total")
