word = input()

while word != "End":
    if word != "SoftUni":
        new_word = ''
        for i in word:
            new_word += i * 2
        print(new_word)

    word = input()