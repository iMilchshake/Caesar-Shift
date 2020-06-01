# Caesar-Shift
Python libary for Caesar-Shift encrypting, decrypting and automatical cracking

## Features
* Encrypting/Decrypting using shift values
* Automatical cracking of Caesar cipher

## Example using a German sentence
```
from caesarshift import shift, decrypt

# Generate Cipher with a shift-value of 13
cipher = shift(plaintext, -13, True)

# Decrypt Cipher
common_german_words = ('der', 'die', 'das', 'ein', 'ich', 'zu', 'von', 'und', 'kann', 'den', 'dies', 'mit')
decrypt_result = decrypt(cipher, common_german_words, 3)
print("shift-value: " + str(decrypt_result[1][0][0]))
print("plaintext: " + decrypt_result[0])
```
