# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted
message = input("Input text to be converted:  ")

# The encryption/decryption key
key = int(input("Pick an integer from 0 through 25 for the encryption/decryption key: "))

# Whether the program encrypts or decrypts
mode = input("Encrypt or Decrypt? ") # Set to either "encrypt" or "decrypt".

# Every possible symbol that can be encrypted
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.@#$%^&*()_-+=~`{[}]|\;:'\",<>/"

# Store the encrypted/decrypted form of the message
translated = " "

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption
        if mode == "Encrypt":
            translatedIndex = symbolIndex + key
        elif mode == "Decrypt":
            translatedIndex = symbolIndex - key

        # Handle wraparound, if needed
        if translatedIndex >= len(SYMBOLS):
           translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex <0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting
        translated = translated + symbol

# Output the translated string
print(translated)
pyperclip.copy(translated)
