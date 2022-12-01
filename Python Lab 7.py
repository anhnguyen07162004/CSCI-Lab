# Anh Nguyen
# Section G
# Lab 7 - Wordle Redux
# References: 
# Time:

import random

word_bank = []

valid_lengths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                 15, 16, 17, 18, 19, 20, 21, 22, 24, 28, 29]

wins = 0
losses = 0
num_guesses_used = 0
play = True

def get_word_bank(word_length):
  with open("dictionary.txt", 'r', encoding='utf-8') as dictionary_file:
    for line in dictionary_file:
      line = line.strip()
      if len(line) == word_length:
        word_bank.append(line)
  return word_bank

def gen_guess_result(new_guess, secret_word, word_length):
  result_list = list('_' * word_length)
  secret_list = list(secret_word)
  for i in range(len(new_guess)):
    if new_guess[i] == secret_list[i]:
      result_list[i] = "x"
      secret_list[i] = "_"
      continue
    else:
      for j in range(len(secret_list)):
        if new_guess[i] == secret_list[j]:
          result_list[i] = "o"
          secret_list[j] = "_"
          break
  return result_list

seed = input("SEED> ")

length_is_valid = False
while not length_is_valid:
  length = int(input("LENGTH> "))
  if length in valid_lengths:
    length_is_valid = True

while play == True:
  while num_guesses_used < 7:
    get_word_bank(length)
    secret = random.choice(word_bank)
    guess = input("GUESS> ")
    print(gen_guess_result(guess, secret, length))
    


print("OUTPUT", wins)
print("OUTPUT", losses)
