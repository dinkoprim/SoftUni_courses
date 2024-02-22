def sorting(integers_as_str):
    list_of_integers = list(map(int, integers_as_str))
    return (f'The minimum number is {min(list_of_integers)}\n'
            f'The maximum number is {max(list_of_integers)}\n'
            f'The sum number is: {sum(list_of_integers)}')


sequence = input().split(' ')
print(sorting(sequence))
