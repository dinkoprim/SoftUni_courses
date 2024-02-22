first_word = input()
second_word = input()
last_printed_string = first_word
for i in range(len(first_word)):
    left_side = second_word[:i+1]
    right_side = first_word[i+1:]
    new_string = left_side + right_side
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string