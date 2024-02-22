def which_is_in(sequence_1, sequence_2):
    result = []
    for element in sequence_1:
        for word in sequence_2:
            if element in word:
                result.append(element)
                break
    return result


user_string_1 = input().split(', ')
user_string_2 = input().split(', ')
print(which_is_in(user_string_1, user_string_2))
