# Author: Tobias Schneider (https://github.com/iMilchshake)
# Usage:
#   decrypt(cipher: str, words: iter, top: int):
#       - Decrypts the 'cipher' by finding 'words' for each possible shift-value (1-25)
#       - Ignores Numbers, punctuations and whitespaces
#       - returns the decrypted cipher and top shift values
#
#   shift(cipher: str, s: int, show_punc: bool):
#       - Shifts each character in 'cipher' by 's'
#       - Removes punctuation if show_punc=False
#       - Ignores Numbers, punctuations and whitespaces
#
#   get_shiftscores(cipher: str, words: iter, top: int):
#       - Calculates scores for each possible shift-value (1-25) by finding 'words'
#
#   removeUmlaute(text: str):
#       - Removes all German umlauts

from operator import itemgetter
import string


def shift(cipher: str, s: int, show_punc: bool):
    o = ""
    if not show_punc:  # remove punctuation
        cipher = cipher.translate(str.maketrans('', '', string.punctuation))

    for c in cipher.lower():
        if c in string.punctuation or c is ' ' or c.isdigit():
            o += c
        else:
            o += chr(((ord(c) + s - ord('a')) % 26) + ord('a'))
    return o


def get_shiftscores(cipher: str, words: iter, top: int):
    scores = list()
    for s in range(1, 26):
        t = shift(cipher, s, False)
        score = 0
        for word in words:
            score += t.count(word)

        scores.append((s, score))

    scores.sort(key=itemgetter(1), reverse=True)  # Sort Scores
    return scores[:top]  # return the best ones


def remove_umlaute(text: str):
    special_char_map = {ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss'}
    return text.translate(special_char_map)


def decrypt(cipher: str, words: iter, top: int):
    top_scores = get_shiftscores(cipher, words, top)
    return shift(cipher, int(top_scores[0][0]), True), top_scores
