# Anh Nguyen
# Section G
# Lab 7 - Wordle Redux
# References: Wordle Lab
# Time: 5 hours

import random

word_bank = []

guess_list = []

valid_lengths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                 15, 16, 17, 18, 19, 20, 21, 22, 24, 28, 29]

wins = 0
losses = 0
num_guesses_used = 0

def get_word_bank(word_length):
  with open("dictionary.txt", 'r', encoding='utf-8') as dictionary_file:
    for line in dictionary_file:
      line = line.strip()
      if len(line) == word_length:
        word_bank.append(line)
  return word_bank

def gen_guess_result(new_guess, secret_word, word_length):
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
  print(f"OUTPUT {' '.join(result_list)}")

def get_guess(guess_list, word_length, word_bank):
    guess_is_valid = False
    while not guess_is_valid:
        # Collects a new guess from the player
        new_guess = input("GUESS> ")

        # Forces all letters to lowercase, just in case
        new_guess = new_guess.lower()

        # Checks new_guess length
        if len(new_guess) != word_length:
            print(f"Please enter a {word_length}-letter word.")

        # Checks if new_guess is a real word
        elif new_guess not in word_bank:
            print(f"Please enter a real word.")

        # Checks if new_guess has been used before
        elif new_guess in guess_list:
            print(f"Please enter a word you haven't guessed yet.")

        else:
            guess_is_valid = True
        guess_list.append(new_guess)
    return new_guess

if __name__ == '__main__':
  seed = input("SEED> ")
  random.seed(seed)
  length_is_valid = False
  while not length_is_valid:
    # TODO: Ask player for the INTEGER length of word to play with
    word_length = int(input("LENGTH> "))

    # Checks if words of the requested length exist in our dictionary
    if word_length in valid_lengths:
      length_is_valid = True

  word_bank = get_word_bank(word_length)
  secret_word = random.choice(word_bank)
  result_list = list('_' * word_length)
  game_result = ""
  play = True
  while play == True:
    while game_result == "":
      user_guess = get_guess(guess_list, word_length, word_bank)
      gen_guess_result(user_guess, secret_word, word_length)
      num_guesses_used += 1
      print(result_list.count("x"))
      if result_list.count("x") == len(result_list):
        game_result = "Won"
        wins += 1
        print("OUTPUT", secret_word)
        print("OUTPUT Won")
      elif num_guesses_used == 6:
        game_result = "Lost"
        losses += 1
        print("OUTPUT", secret_word)
        print("OUTPUT Lost")
    choice = input("CONTINUE> ")
    if choice == "Yes":
      play = True
    else:
      play = False
    game_result = ""
    secret_word = random.choice(word_bank)
  print("OUTPUT", wins)
  print("OUTPUT", losses)
