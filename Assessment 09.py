# Anh Nguyen
# CSCI 102 - Section B
# Assessment 09
# References: Wordle Lab
# Time: 25 minutes

import random
valid_lengths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                 15, 16, 17, 18, 19, 20, 21, 22, 24, 28, 29]
word_length = int(input("LENGTH> "))
seed = input("SEED> ")

length_is_valid = False
  
word_bank = []

with open("dictionary.txt", 'r', encoding='utf-8') as dictionary_file:
  for line in dictionary_file:
    line = line.strip()
    if len(line) == word_length:
      word_bank.append(line)



print("OUTPUT", len(word_bank))

if len(word_bank) == 0:
  print("OUTPUT None")
else:
  random.seed(seed)
  word = random.choice(word_bank)
  print("OUTPUT", word)
