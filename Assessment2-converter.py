# Anh Nguyen
# CSCI 101 - Section G
# Assessment 2
# References: Professor showed how to know if a string has invalid input, searched how to reverse a list
# Time: 3 hours

run = True # Used so I can put everything in a loop and break out when needed
index = 0 # Initial variable to use as index in loop
index2 = 0
choice = int(input("OPTION> ")) # Input to choose which converter to use
sum = 0 # Will be used to count what the binary number is in decimal
length = 0 # Will be set to the length of binary str or decimal str
power = 0 # Will be used to help with calculating decimal value
remainder = 0 # Will be used to convert decimal to binary
remainder_result = []
binary_result = ""

while run == True:
  if choice == 1:
    binary_str = input("BINARY-STR> ")
    if (binary_str.count("0") + binary_str.count("1")) != len(binary_str):
      print("OUTPUT ERROR")
      break
    else:
      length = len(binary_str)
      power = length - 1
      while index < length:
        if binary_str[index] == "1":
          sum += 2 ** power
        index += 1
        power -= 1
    print("OUTPUT", sum)
    run = False
  elif choice == 2:
    dec_str = input("DECIMAL-STR> ")
    if dec_str[0] == "0":
      print("OUTPUT 0")
      break
    if (dec_str.count("0") + dec_str.count("1") + dec_str.count("2") + dec_str.count("3") + dec_str.count("4") + dec_str.count("5") + dec_str.count("6") + dec_str.count("7") + dec_str.count("8") + dec_str.count("9") != len(dec_str)):
      print("OUTPUT ERROR")
      break
    else:
      int_dec_str = int(dec_str)
      while int_dec_str != 0:
        remainder = int_dec_str % 2
        int_dec_str = int_dec_str // 2
        remainder_result.append(remainder)
      remainder_result.reverse()
      while index2 < len(remainder_result):
        binary_result = binary_result + str(remainder_result[index2])
        index2 += 1
    print("OUTPUT", binary_result)
    run = False
