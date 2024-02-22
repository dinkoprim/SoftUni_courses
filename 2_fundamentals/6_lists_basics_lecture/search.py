n = int(input())
special_word = input()
list_of_strings = []
sorted_strings = []
for _ in range(n):
    given_strings = input()
    list_of_strings.append(given_strings)

print(list_of_strings)

for given_strings in list_of_strings:
    if special_word in given_strings:
        sorted_strings.append(given_strings)

print(sorted_strings)
