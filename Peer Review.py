# Anh Nguyen
# CSCI 102 - Section B
# Assessment 06B
# References: None
# Time: 

count = 0 # Count iterations
amount = int(input("COUNT> ")) # Gets the amount of numbers to be input
nums_list = [] # Setting up an empty list to store the numbers input

for i in range(amount):
  user_input = float(input("NUMBER> "))
  nums_list.append(user_input)

for i in range(len(nums_list)):
  initial_guess = 10
  better_guess = 0.0
  count = 1
  while initial_guess != better_guess:
    better_guess = better_guess = (initial_guess + nums_list[i] / initial_guess) / 2
    if initial_guess != better_guess:
      initial_guess = better_guess
      count += 1
      better_guess = 0.0
    elif initial_guess == better_guess:
      break
  print(f"OUTPUT After {count} iterations, {nums_list[i]}^0.5 = {initial_guess:.2f}")
