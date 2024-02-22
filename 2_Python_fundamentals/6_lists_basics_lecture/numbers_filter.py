n = int(input())
list_of_all_ints = []
even_list = []
odd_list = []
negative_list = []
positive_list = []
for _ in range(n):
    user_integers = int(input())
    list_of_all_ints.append(user_integers)
command = input()
for user_integers in list_of_all_ints:
    if user_integers % 2 == 0:
        even_list.append(user_integers)
    elif user_integers % 2 != 0:
        odd_list.append(user_integers)
    if user_integers >= 0:
        positive_list.append(user_integers)
    elif user_integers < 0:
        negative_list.append(user_integers)

if command == 'positive':
    print(positive_list)
elif command == 'negative':
    print(negative_list)
elif command == 'even':
    print(even_list)
elif command == 'odd':
    print(odd_list)