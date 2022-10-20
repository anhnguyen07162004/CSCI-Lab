# Anh Nguyen
# CSCI 102 – Section C
# Assessment 08A
# References: https://www.w3schools.com/ to learn more about random in Python
# Time: 30 minutes

import random

roll_list = [] # Making list to track rolls made
seed = int(input())
sides = int(input())
rolls = int(input())

random.seed(seed)

# Appending the list by sides
for i in range (0, sides):
  roll_list.append(0)

# Rolling the dice by rolls
for j in range(0, rolls):
  num = random.randint(1, sides)
  roll_list[num-1] += 1

# Printing outputs from list
for v in range(0, len(roll_list)):
  print(f"OUTPUT {v+1} occurred {roll_list[v]} times")
