# Name: Anh Nguyen
# CSCI 101 – Section G
# Python Assessment 3
# References: Learned I needed to do import string from website: geeksforgeeks.com
# Time: 2 hours

import string

with open("peter_pan.txt", 'r+', encoding = 'utf-8') as file:
  contents = file.read()
  new_contents = contents.replace("-", " ")
  new_contents = new_contents.replace("\n", " ")
  new_contents = new_contents.translate(str.maketrans('', '', string.punctuation))
  new_contents = new_contents.lower()

choice = input("CHOICE> ")

if choice == "1":
  word_choice = input("WORD> ")
  low_word_choice = word_choice.lower()
  count = 0
  new_contents_list = new_contents.split(" ")
  for i in range(len(new_contents_list)):
    if new_contents_list[i] == low_word_choice:
      count += 1
  print("OUTPUT", count)
if choice == "2":
  word_length = int(input("LENGTH> "))
  count = 0
  new_contents_list = new_contents.split(" ")
  for i in range(len(new_contents_list)):
    if len(new_contents_list[i]) == word_length:
      count += 1
  print("OUTPUT", count)
  unique_list = []
  for i in range(len(new_contents_list)):
    if new_contents_list[i] not in unique_list and len(new_contents_list[i]) == word_length:
      unique_list.append(new_contents_list[i])
  print("OUTPUT", len(unique_list))
