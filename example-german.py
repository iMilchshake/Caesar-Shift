from caesarshift import remove_umlaute, shift, decrypt

# This Example uses a German sentence and common German words, but this will work with every language

# Generate Cipher with a shift-value of 13
plaintext = "...und den Gorillas, die stehend bis zu 1,75 Meter hoch werden und ein Gewicht von 200 Kilogramm " \
            "erreichen können, sowie den Menschen mit einer Körpergröße von durchschnittlich 1,60 bis 1,80 Metern, " \
            "in Einzelfällen auch mehr als 2,00 Metern. Einige Arten haben einen ausgeprägten... "
plaintext_withoutUmlaute = remove_umlaute(plaintext)
cipher = shift(plaintext_withoutUmlaute, -13, True)

# Decrypt Cipher
common_german_words = ('der', 'die', 'das', 'ein', 'ich', 'zu', 'von', 'und', 'kann', 'den', 'dies', 'mit')
decrypt_result = decrypt(cipher, common_german_words, 3)
print("shift-value: " + str(decrypt_result[1][0][0]))
print("plaintext: " + decrypt_result[0])