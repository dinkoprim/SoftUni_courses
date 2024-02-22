fruit_name = str(input())
result = 'unknown'
if fruit_name == 'banana' or fruit_name == 'apple' \
    or fruit_name == 'kiwi' or fruit_name == 'cherry' \
    or fruit_name == 'lemon' or fruit_name == 'grapes':
    result = 'fruit'
elif fruit_name == 'tomato' or fruit_name == 'cucumber' \
    or fruit_name == 'pepper' or fruit_name == 'carrot':
    result = 'vegetable'
print(result)
