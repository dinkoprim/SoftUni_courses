def is_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


user_list = input().split(', ')
for number in user_list:
    print(is_palindrome(number))