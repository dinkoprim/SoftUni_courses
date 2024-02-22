def decipher(words):
    deciphered_words = []
    for word in words:
        digits = [digit for digit in word if digit.isdigit()]
        letters = [char for char in word if not char.isdigit()]
        letters[0], letters[-1] = letters[-1], letters[0]
        if digits:
            secret_letter = chr(int(''.join(digits)))
            letters.insert(0, secret_letter)
        deciphered_words.append(''.join(letters))
    return ' '.join(deciphered_words)


user_string = input().split()
print(decipher(user_string))