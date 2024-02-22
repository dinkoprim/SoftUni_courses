total_sum = 0
number_of_characters = int(input())
for i in range(number_of_characters):
    letter = input()
    total_sum += ord(letter)
print(f'The sum equals: {total_sum}')