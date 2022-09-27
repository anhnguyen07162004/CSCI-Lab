# Anh Nguyen
# CSCI 101 – Section G
# Python Lab 3
# References: Found out about "not in" from Google
# Time: 3+ hours.... a lot of debugging and all code from me

# Initial variable to easily track the winner
winner = ""

# Getting inputs
table_size = int(input("SIZE> "))
row_1 = input("ROW0 ")
row_2 = input("ROW1 ")
row_3 = input("ROW2 ")

# Checking if the table is valid, and getting the winner
if len(row_1) != table_size or len(row_2) != table_size or len(row_3) != table_size:
  print("OUTPUT ERROR")
elif "X" not in row_1 and "O" not in row_1 and "E" not in row_1:
  print("OUTPUT ERROR")
elif "X" not in row_2 and "O" not in row_2 and "E" not in row_2:
  print("OUTPUT ERROR")
elif "X" not in row_3 and "O" not in row_3 and "E" not in row_3:
  print("OUTPUT ERROR")
else:
  if row_1[0] == "X" and row_1[1] == "X" and row_1[2] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_1[0] == "O" and row_1[1] == "O" and row_1[2] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_2[0] == "X" and row_2[1] == "X" and row_2[2] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_2[0] == "O" and row_2[1] == "O" and row_2[2] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_3[0] == "X" and row_3[1] == "X" and row_3[2] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_3[0] == "O" and row_3[1] == "O" and row_3[2] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_1[0] == "X" and row_2[0] == "X" and row_3[0] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_1[0] == "O" and row_2[0] == "O" and row_3[0] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_1[1] == "O" and row_2[1] == "O" and row_3[1] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_1[2] == "O" and row_2[2] == "O" and row_3[2] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_1[0] == "O" and row_2[1] == "O" and row_3[2] == "O":
    winner = "O"
    print("OUTPUT", winner)
  elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
    winner = "X"
    print("OUTPUT", winner)
  elif row_1[2] == "O" and row_2[1] == "O" and row_3[0] == "O":
    winner = "O"
    print("OUTPUT", winner)
  else:
    winner = "N"
    print("OUTPUT", winner)
