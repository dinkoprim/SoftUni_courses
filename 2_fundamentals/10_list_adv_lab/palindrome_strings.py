def is_palindrome(word):
    if word == word[::-1]:
        return word


def palindrome_check(string, palindrome):
    words = string.split()
    palindromes_list = [word for word in words if is_palindrome(word)]
    searched_word_count = palindromes_list.count(palindrome)
    result = '\n'.join([str(palindromes_list), f'Found palindrome {searched_word_count} times'])
    return result


user_string = input()
user_palindrome = input()
print(palindrome_check(user_string, user_palindrome))
