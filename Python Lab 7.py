# Anh Nguyen
# CSCI 102 Section B
# Assessment 13
# References: Google for ord function, Asked for help with decrypt function online
# Time: 3-4 hours

def encrypt(text, shift):
  encrypted_text = ""

  for char in text:
    if char.isalpha():
      if char.isupper():
        shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
      else:
        shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
      shifted_char = char
    encrypted_text += shifted_char
  print("OUTPUT", encrypted_text)

def decrypt(encrypted_text):

  for shift in range(1, 26):
    decrypted_text = ""
    for i, char in enumerate(encrypted_text):
      char_index = ord(char) - ord('A')
      decrypted_char_index = (char_index - (shift - i) % 26) % 26
      decrypted_char = chr(decrypted_char_index + ord('A'))

      decrypted_text += decrypted_char

    if decrypted_text.isalpha():
      print("OUTPUT", decrypted_text)
      print("OUTPUT", shift)
      break


if __name__ == "__main__":
    print(
        "Welcome to our Caesar Cipher Algorithm!\n" +
        "Choose one of the following methods:\n" +
        "\t1 - Encryption\n" +
        "\t2 - Decryption"
    )
    while True:
        userIn = str(input("OPERATION> "))

        # If the user inputs 1, for encryption
        if userIn == "1":
            str = input("MESSAGE> ")
            shift = int(input("SHIFT> "))
            encrypt(str, shift)
            break

        # If the user inputs 2, for encryption
        elif userIn == "2":
            str2 = input("MESSAGE_TO_DECRYPT> ")
            decrypt(str2)
            break

        else:
            print("Invalid Operation!")
