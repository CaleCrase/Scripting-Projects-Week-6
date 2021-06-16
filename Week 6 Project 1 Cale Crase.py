"""
Program: Project1 Crase
Author: Cale Crase
Caesar Cipher
"""

text = input("Enter text to be ciphered: ")
distance = int(input("What is the distance value: "))
code = " "
for ch in text:
  ordvalue = ord(ch)
  cipherValue = ordvalue + distance
  if cipherValue > ord('z'):
    cipherValue = ord('a') + distance - \
                  (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
    print(code)
