# Anh Nguyen
# CSCI 102 – Section B
# Assessment 02B
# Googled how to slice a string (found out inclusive and exclusive)
# Time: 20 minutes

# Saves input as variable
print("Enter your string: ")
str1 = input("STRING> ")

# Saves inputs as integers
print("Enter four numbers to slice the string")
num1 = int(input("A> "))
num2 = int(input("B> "))
num3 = int(input("C> "))
num4 = int(input("D> "))

word1 = str1[num1 + 1:num2]
word2 = str1[num3 + 1: num4]

print("OUTPUT", word1, word2)
