user_text = input()

user_text_set = set(user_text)

formatted_set = [f'{char}: {user_text.count(char)} time/s'
                 for char in sorted(user_text_set)]

print(*formatted_set, sep='\n')